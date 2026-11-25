import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Sum of quadratic terms with different scales and offsets
        result = 0.0
        
        # Global minimum at origin
        result += np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * np.sin(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        return result