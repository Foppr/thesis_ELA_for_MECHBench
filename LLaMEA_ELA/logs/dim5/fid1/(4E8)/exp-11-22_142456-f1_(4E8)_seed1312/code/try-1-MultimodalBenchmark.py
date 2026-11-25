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
        
        # Add multiple local minima using trigonometric terms
        for i in range(self.dim):
            result += 10 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[(i + 1) % self.dim])
        
        # Add a small noise term to increase complexity
        result += 0.1 * np.sum(np.sin(x))
        
        return result