import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.01 * np.sum(np.abs(x))
        
        return f_val