import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with adaptive scaling
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1) * 0.5
        
        # Add multiple local minima using coupled trigonometric terms
        for i in range(self.dim):
            result += 5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[(i + 1) % self.dim]) * (1 + 0.1 * np.sin(0.3 * x[i]))
        
        # Add cross-dimensional interactions with higher-order terms
        for i in range(self.dim):
            result += 2 * np.sin(x[i]) * np.cos(x[(i + 2) % self.dim]) * np.sin(0.5 * x[(i + 1) % self.dim])
        
        # Add a small noise term to increase complexity
        result += 0.05 * np.sum(np.sin(x) * np.cos(0.5 * x))
        
        return result