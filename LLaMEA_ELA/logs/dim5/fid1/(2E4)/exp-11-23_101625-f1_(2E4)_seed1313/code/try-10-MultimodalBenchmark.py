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
        
        # Add multiple local minima using cosine terms with varying frequencies
        for i in range(self.dim):
            result += 0.15 * np.cos(7 * x[i]) * np.exp(-0.05 * (x[i] - 1)**2)
            
        # Add interaction terms between dimensions with higher frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(5 * x[i]) * np.cos(3 * x[j])
                
        # Add a global minimum at the origin with additional penalty
        result += 0.03 * np.sum((x - 0.5)**2)
        
        # Add a periodic component to increase multimodality
        for i in range(self.dim):
            result += 0.1 * np.sin(4 * x[i]) * np.cos(6 * x[i])
            
        return result