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
        
        # Add multiple local minima using combined trigonometric terms
        for i in range(self.dim):
            result += 5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[(i + 1) % self.dim]) * (1 + 0.1 * np.sin(0.3 * x[i]))
        
        # Add higher frequency oscillations for increased complexity
        for i in range(self.dim):
            result += 2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[(i + 2) % self.dim])
        
        # Add a small noise term to increase complexity
        result += 0.05 * np.sum(np.sin(x))
        
        return result