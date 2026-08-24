import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squared terms with different coefficients
        result = np.sum(x**2)
        
        # Add multiple local minima using sine terms
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        result += 0.01 * np.sum(np.abs(x))
        
        return result