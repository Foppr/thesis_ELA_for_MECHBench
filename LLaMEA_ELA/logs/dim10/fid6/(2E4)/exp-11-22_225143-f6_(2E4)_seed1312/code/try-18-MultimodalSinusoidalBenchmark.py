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
        
        # Enhanced sinusoidal modulations with varying frequencies and chaotic interactions
        for i in range(self.dim):
            f_val += 0.5 * np.sin(5 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i])
            f_val += 0.3 * np.sin(7 * np.pi * x_norm[i]**3) * np.cos(6 * np.pi * x_norm[i]**2)
        
        # Stronger interaction terms between dimensions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.4 * np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(5 * np.pi * (x_norm[i] - x_norm[j]))
                f_val += 0.2 * np.sin(2 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(4 * np.pi * (x_norm[i]*x_norm[j]))
        
        # Additional complex global structure with multiple peaks and nested patterns
        f_val += 0.6 * np.sum(np.sin(8 * np.pi * x_norm)**2)
        f_val += 0.3 * np.sum(np.sin(10 * np.pi * x_norm**3)**2)
        
        # Add a more challenging basin around the origin with non-separable terms
        f_val += 0.2 * np.sum((x_norm**6) * np.cos(3 * np.pi * x_norm))
        f_val += 0.1 * np.sum(np.sin(9 * np.pi * x_norm) * (x_norm**2))
        
        # Introduce chaotic behavior through exponential modulation
        f_val += 0.15 * np.sum(np.exp(-x_norm**2) * np.sin(6 * np.pi * x_norm))
        
        return f_val