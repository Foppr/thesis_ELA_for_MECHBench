import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for consistency
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f_val = 0.5 * np.sum(x_norm**2)
        
        # Enhanced sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Stronger interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Additional complex global structure with multiple peaks
        f_val += 0.4 * np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Add a more challenging basin around the origin
        f_val += 0.1 * np.sum((x_norm**4) * np.cos(2 * np.pi * x_norm))
        
        return f_val