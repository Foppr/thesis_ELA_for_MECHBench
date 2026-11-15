import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Sum of quadratic terms with different scales and offsets
        result = 0.0
        
        # Global minimum at origin
        result += np.sum(x**2)
        
        # Add multiple local minima with modified frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Add more complex interactions with higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(2 * x[i] - x[j])
        
        # Add noise-like component with different frequencies
        result += 0.07 * np.sum(np.sin(12 * x) + np.cos(9 * x))
        
        # Add a small cubic term to increase nonlinearity
        result += 0.005 * np.sum(x**3)
        
        return result