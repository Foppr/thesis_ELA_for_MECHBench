import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sine-wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.6 * np.sin(12 * np.pi * x[i]) + 0.35 * np.sin(24 * np.pi * x[i]) + \
                     0.25 * np.sin(48 * np.pi * x[i]) + 0.15 * np.sin(96 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(0.5 * i) - 1.25
            width = 0.06 + 0.12 * np.cos(0.3 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.12 * (1 + np.sin(0.75 * (i + j)))
                f_val += coupling * np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(3.5 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.12 * (x[i]**3) * (1 + 0.25 * np.sin(5.5 * x[i])) + \
                     0.06 * (x[i]**5) * (1 + 0.12 * np.cos(3.5 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.09 * np.sin(5.5 * x[i]) * np.cos(4.5 * x[j]) * \
                         np.exp(-0.12 * (x[i] - x[j])**2) * (1 + 0.35 * np.sin(2.2 * (x[i] + x[j])))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.25 * np.sin(2.2 * np.pi * np.sum(x)) + 0.18 * np.cos(3.2 * np.pi * np.sum(x)) + \
                 0.12 * np.sin(5.2 * np.pi * np.sum(x)**2) + 0.06 * np.cos(7.2 * np.pi * np.sum(x)**3)
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 12 * (abs(x[i]) - 4.5)**2
        f_val += penalty
        
        return f_val