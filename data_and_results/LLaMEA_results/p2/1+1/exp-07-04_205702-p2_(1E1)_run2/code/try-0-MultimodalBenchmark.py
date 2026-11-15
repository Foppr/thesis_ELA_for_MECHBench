import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        f2 = 0.1 * np.sum(np.sin(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Add a global minimum at origin with additional penalty terms
        f3 = 0.01 * np.sum(np.abs(x)**3)
        
        return f1 + f2 + f3