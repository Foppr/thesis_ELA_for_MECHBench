import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.8
        self.seed = 0.2
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial potential with mixed degrees
        f_val = 0.3 * np.sum(x**4) / self.dim + 0.7 * np.sum(x**2) / self.dim
        
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            f_val += 1.0 * np.sin(3 * x[i]) * np.cos(2 * x[i % (self.dim-1)] if self.dim > 1 else x[i])
            
        # Multi-scale Gaussian peaks with varying heights and widths
        num_peaks = min(7, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 1.0 * i
            width = 0.3 + 0.4 * np.cos(i * 0.5)
            height = 0.8 + 0.6 * np.sin(i * 0.8)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic modulation using tent map
        chaos_val = self.seed
        for i in range(self.dim):
            if chaos_val < 0.5:
                chaos_val = 2 * chaos_val
            else:
                chaos_val = 2 * (1 - chaos_val)
            f_val += 0.5 * chaos_val * np.sin(0.7 * x[i % self.dim])
            
        # Adaptive scaling based on local gradient magnitude
        grad_magnitude = np.mean(np.abs(np.gradient(x)))
        scale_factor = 1.0 + 0.5 * grad_magnitude
        f_val *= scale_factor
        
        # Cross-dimensional interaction through product terms
        if self.dim >= 3:
            for i in range(0, self.dim - 2):
                f_val += 0.3 * x[i] * x[i+1] * x[i+2]
                
        return f_val