import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add multiple local minima using more complex sinusoidal terms
        for i in range(self.dim):
            f += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            
        # Add additional interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.1 * np.sin(3 * x[i]) * np.sin(2 * x[(i + 2) % self.dim])
            
        # Add a global minimum at origin with modified penalty terms
        f += 0.02 * np.sum(np.abs(x)) + 0.005 * np.sum(x**4)
        
        return f