import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += (0.3 * np.sin(12 * x[i]) + 0.2 * np.cos(15 * x[i]) + 
                     0.1 * np.sin(25 * x[i]) + 0.05 * np.cos(30 * x[i]))
        
        # Add radial basis components with chaotic centers and varying widths
        for i in range(self.dim):
            center = 3.0 * np.sin(0.4 * i) - 1.5
            width = 0.02 + 0.08 * np.cos(0.5 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional coupling with chaotic coupling strengths and sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.15 * (1 + 0.3 * np.sin(0.8 * (i - j)))
                f_val += coupling * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
        
        # Add chaotic polynomial conditioning with adaptive exponents
        for i in range(self.dim):
            exponent = 2 + 0.5 * np.sin(0.6 * i)
            f_val += 0.1 * (x[i]**exponent) * (1 + 0.3 * np.cos(2 * x[i]))
        
        # Add multi-scale chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(3 * x[i]) * np.cos(5 * x[j]) * \
                         np.exp(-0.2 * (x[i] - x[j])**2) * (1 + 0.2 * np.sin(3 * (x[i] + x[j])))
        
        # Add global chaotic modulation with multiple harmonic components
        f_val += 0.25 * np.sin(3 * np.sum(x)) + 0.18 * np.cos(4 * np.sum(x)) + \
                 0.12 * np.sin(6 * np.sum(x)**2) + 0.08 * np.cos(8 * np.sum(x)**3)
        
        # Add sharp gradient penalties at boundary regions with chaotic scaling
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.6:
                scale = 1.0 + 0.2 * np.sin(0.5 * i)
                penalty += scale * (abs(x[i]) - 4.6)**3
        f_val += penalty
        
        return f_val