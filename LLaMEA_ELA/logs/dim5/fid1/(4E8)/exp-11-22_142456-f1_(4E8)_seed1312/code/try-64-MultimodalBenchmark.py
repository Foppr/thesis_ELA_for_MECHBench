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
            result += (x[i] ** 2) * (1 + 0.1 * i)
        
        # Add multiple local minima using coupled trigonometric terms
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add higher-order polynomial interactions for increased complexity
        for i in range(self.dim):
            result += 0.5 * (x[i] ** 4) * np.sin(0.3 * x[i])
        
        # Add cross-dimensional coupling with sine waves
        cross_term = 0.0
        for i in range(self.dim):
            cross_term += np.sin(0.5 * x[i]) * np.cos(0.2 * x[(i + 2) % self.dim])
        result += 3 * cross_term ** 2
        
        # Add a small noise term to increase complexity
        result += 0.05 * np.sum(np.sin(x))
        
        return result