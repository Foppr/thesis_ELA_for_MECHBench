import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Sum of quadratic terms with different scales and offsets
        result = 0.0
        for i in range(self.dim):
            # Add multiple quadratic terms with different coefficients
            result += (x[i] - 1.0)**2 + (x[i] + 1.0)**2 + 0.1 * np.sin(5.0 * x[i])
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * (x[i] - x[j])**2
        
        # Add a global minimum at origin with additional penalty
        result += 0.5 * np.sum(x**2)
        
        return result