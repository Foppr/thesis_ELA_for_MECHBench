import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Sum of quadratic terms with different coefficients and shifts
        result = 0.0
        
        # Main quadratic term centered at origin
        result += np.sum(x**2)
        
        # Add multiple local minima using cosine terms
        for i in range(self.dim):
            result += 0.1 * np.cos(5 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * np.sin(3 * x[i]) * np.cos(2 * x[j])
                
        # Add a global minimum at the origin with additional penalty
        result += 0.05 * np.sum((x - 1)**2)
        
        return result