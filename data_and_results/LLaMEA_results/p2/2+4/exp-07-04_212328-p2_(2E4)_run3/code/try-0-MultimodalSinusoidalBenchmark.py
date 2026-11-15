import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add sinusoidal grid pattern with multiple global minima
        for i in range(self.dim):
            f += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add a global minimum at the origin with additional noise
        f += 0.01 * np.sum(np.sin(x)**2)
        
        return f