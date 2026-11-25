import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squared terms with different scales
        result = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal components
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        for i in range(self.dim):
            result += 0.01 * (x[i] - 2)**4 + 0.005 * (x[i] + 3)**6
            
        return result