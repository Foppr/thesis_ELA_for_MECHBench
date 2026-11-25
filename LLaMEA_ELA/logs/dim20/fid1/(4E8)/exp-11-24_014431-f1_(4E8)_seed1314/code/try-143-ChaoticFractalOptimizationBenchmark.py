import numpy as np

class ChaoticFractalOptimizationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 1.2 * np.sin(15 * x[i]) + 0.8 * np.cos(25 * x[i]) + \
                     0.6 * np.sin(40 * x[i]) + 0.4 * np.cos(60 * x[i]) + \
                     0.2 * np.sin(80 * x[i])
        
        # Add adaptive polynomial conditioning with dynamic exponents
        for i in range(self.dim):
            exponent = 3 + 2 * np.sin(0.5 * i)
            f_val += 0.3 * (x[i]**exponent) * (1 + 0.3 * np.cos(5 * x[i]))
        
        # Add fractal-like self-similar structures with recursive scaling
        scale_factor = 0.2
        for k in range(1, 8):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 20 * x[i]) * np.cos(k * 15 * x[i])
            scale_factor *= 0.4
        
        # Add dynamic coupling terms with adaptive strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.25 * (1 + np.sin(0.7 * i) * np.cos(0.7 * j))
                f_val += coupling_strength * np.exp(-0.3 * (x[i] - x[j])**2) * \
                         np.sin(5 * (x[i] + x[j]))
        
        # Add boundary-sensitive penalties with varying intensities
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 15 * (abs(x[i]) - 4.5)**3
        f_val += penalty
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * np.sin(6 * x[i]) * np.cos(5 * x[j]) * \
                         np.exp(-0.2 * (x[i] - x[j])**2) * (1 + 0.4 * np.sin(3 * (x[i] + x[j])))
        
        # Add global correlation components with varying weights
        f_val += 0.5 * np.sin(3 * np.sum(x)) + 0.3 * np.cos(4 * np.sum(x)) + \
                 0.2 * np.sin(6 * np.sum(x)**2) + 0.1 * np.cos(8 * np.sum(x)**3)
        
        # Add cubic coupling terms with chaotic phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.06 * (x[i]**3) * np.sin(3 * x[j] + 0.5 * i) + \
                         0.05 * (x[j]**3) * np.cos(3 * x[i] + 0.5 * j)
        
        return f_val