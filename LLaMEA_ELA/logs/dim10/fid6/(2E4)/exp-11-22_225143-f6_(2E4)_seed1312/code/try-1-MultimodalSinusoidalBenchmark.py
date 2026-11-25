import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for consistency
        x_norm = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_norm**2)
        
        # Add sinusoidal modulations in each dimension
        for i in range(self.dim):
            f_val += 0.5 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Add a global minimum at the origin with additional complexity
        f_val += 0.3 * np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        return f_val