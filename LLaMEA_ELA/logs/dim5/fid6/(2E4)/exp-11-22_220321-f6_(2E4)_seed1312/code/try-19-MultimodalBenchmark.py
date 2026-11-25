import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add multiple local minima using sine waves with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            
        # Add a more complex penalty term to make the landscape more challenging
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i] - 2.0)**6 + (x[i] + 2.0)**6 + (x[i] ** 4) * np.sin(5 * x[i])
            
        # Add cross-dimensional interactions
        for i in range(self.dim):
            result += 0.1 * x[i] * x[(i + 1) % self.dim] * np.sin(2 * x[i]) * np.cos(3 * x[(i + 2) % self.dim])
            
        return result + 0.02 * penalty