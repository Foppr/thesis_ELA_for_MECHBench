import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = np.sum(x**2) * (1.0 + 0.2 * np.sin(0.3 * np.sum(x**2)))
        
        # Enhanced oscillatory components with varying frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * abs(x[i]))
            
        # Modified saddle structure with enhanced directional dependency
        if self.dim >= 2:
            diff_sum = 0
            for i in range(self.dim - 1):
                diff_sum += (x[i] - x[i+1])**2 * (1.0 + 0.1 * np.sin(x[i] * x[i+1]) * np.cos(0.5 * x[i]))
            f_val += 0.2 * diff_sum
            
        # Multiple interacting Gaussian peaks with complex positioning
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                f_val += 0.25 * np.exp(-0.5 * ((x[i] - 1.5)**2 + (x[i+1] + 1.5)**2 + (x[i+2] - 1.0)**2))
                
        # Additional high-frequency noise terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.2 * abs(x[i]))
            
        # Cross-dimensional interaction terms
        if self.dim >= 3:
            interaction_sum = 0
            for i in range(self.dim - 2):
                interaction_sum += x[i] * x[i+1] * x[i+2] * np.sin(0.4 * (x[i] + x[i+1] + x[i+2]))
            f_val += 0.15 * interaction_sum
            
        return f_val