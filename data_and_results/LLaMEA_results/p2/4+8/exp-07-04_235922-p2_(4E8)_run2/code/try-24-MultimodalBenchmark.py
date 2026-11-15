import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with shifted frequencies
        f2 = 0.15 * np.sum(np.sin(6.0 * x + 1.0) * np.exp(-0.15 * x**2))
        
        # Add a global minimum at origin with additional complexity
        f3 = 0.02 * np.sum(np.cos(12.0 * x - 2.0) * np.exp(-0.07 * x**2))
        
        # Add interaction terms between dimensions
        f4 = 0.05 * np.sum((x[:-1] - x[1:]) ** 2)
        
        # Combine all terms
        return f1 + f2 + f3 + f4