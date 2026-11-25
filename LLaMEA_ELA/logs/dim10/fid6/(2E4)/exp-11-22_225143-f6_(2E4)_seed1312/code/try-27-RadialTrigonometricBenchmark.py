import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with enhanced conditioning
        f_val = 0.4 * np.sum(x_norm**2)
        
        # Enhanced radial basis functions with stronger interactions
        for i in range(self.dim):
            # Multi-scale Gaussian-like radial terms
            f_val += 0.6 * np.exp(-3.0 * np.sum((x_norm - np.sin(i * np.pi / self.dim))**2))
            f_val += 0.4 * np.exp(-2.0 * np.sum((x_norm - np.cos(i * np.pi / self.dim))**2))
            # Additional radial terms with different patterns
            f_val += 0.2 * np.exp(-1.0 * np.sum((x_norm - np.tan(i * np.pi / (self.dim + 1)))**2))
        
        # Stronger trigonometric coupling terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher frequency trigonometric interactions
                f_val += 0.3 * np.sin(6 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
                f_val += 0.2 * np.cos(7 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(3 * np.pi * (x_norm[i]*x_norm[j]))
                # Cross-dimensional coupling with non-linear interaction
                f_val += 0.15 * np.sin(5 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[j]) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Enhanced adaptive conditioning with more complex decay
        for i in range(self.dim):
            f_val += 0.2 * np.exp(-np.abs(x_norm[i]) * (1.5 + 0.8 * np.sin(9 * np.pi * x_norm[i])))
            # Additional non-linear conditioning term
            f_val += 0.1 * np.sin(4 * np.pi * x_norm[i])**2 * np.cos(3 * np.pi * x_norm[i])
        
        # Enhanced nested periodic patterns with higher frequencies
        f_val += 0.3 * np.sum(np.sin(8 * np.pi * x_norm)**4)
        f_val += 0.15 * np.sum(np.cos(10 * np.pi * x_norm**2)**2)
        
        # Increased non-separable high-order interaction terms
        f_val += 0.1 * np.sum((x_norm**5 + x_norm**4 + x_norm**3) * np.sin(5 * np.pi * x_norm))
        
        # Stronger chaotic modulation through complex sine-cosine combinations
        f_val += 0.15 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * np.exp(-x_norm**2))
        f_val += 0.1 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * np.tanh(x_norm))
        
        # Additional coupling between all dimensions
        f_val += 0.08 * np.prod(np.sin(np.pi * x_norm)) + 0.05 * np.prod(np.cos(np.pi * x_norm))
        
        return f_val