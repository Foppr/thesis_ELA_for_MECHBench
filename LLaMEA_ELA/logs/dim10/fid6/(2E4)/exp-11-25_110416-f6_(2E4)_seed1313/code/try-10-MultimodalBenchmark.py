import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squared terms with different scales
        result = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal components with modified frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        for i in range(self.dim):
            result += 0.02 * (x[i] - 1.5)**4 + 0.003 * (x[i] + 2.5)**6
            
        return result