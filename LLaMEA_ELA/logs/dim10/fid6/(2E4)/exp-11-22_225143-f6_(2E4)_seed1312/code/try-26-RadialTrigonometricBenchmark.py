import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        f_val = 0.3 * np.sum(x_norm**2)
        
        # Radial basis functions with varying widths and heights
        for i in range(self.dim):
            # Gaussian-like radial terms with different scales
            f_val += 0.5 * np.exp(-2.0 * np.sum((x_norm - np.sin(i * np.pi / self.dim))**2))
            f_val += 0.3 * np.exp(-1.5 * np.sum((x_norm - np.cos(i * np.pi / self.dim))**2))
        
        # Trigonometric coupling terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(4 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(3 * np.pi * (x_norm[i] - x_norm[j]))
                f_val += 0.1 * np.cos(5 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(2 * np.pi * (x_norm[i]*x_norm[j]))
        
        # Adaptive conditioning with exponential decay
        for i in range(self.dim):
            f_val += 0.15 * np.exp(-np.abs(x_norm[i]) * (1 + 0.5 * np.sin(7 * np.pi * x_norm[i])))
        
        # Nested periodic patterns with varying frequencies
        f_val += 0.25 * np.sum(np.sin(6 * np.pi * x_norm)**3)
        f_val += 0.1 * np.sum(np.cos(8 * np.pi * x_norm**2))
        
        # Non-separable high-order interaction terms
        f_val += 0.05 * np.sum((x_norm**4 + x_norm**3) * np.sin(4 * np.pi * x_norm))
        
        # Chaotic modulation through sine-cosine combinations
        f_val += 0.1 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * np.exp(-x_norm**2))
        
        return f_val