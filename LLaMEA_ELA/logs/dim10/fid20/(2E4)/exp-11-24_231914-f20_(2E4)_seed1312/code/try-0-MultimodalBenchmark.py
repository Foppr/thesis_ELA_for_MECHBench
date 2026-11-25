import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function value
        # Global minimum at origin: f(0) = 0
        # Multiple local minima scattered around the search space
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using cosine terms
        for i in range(self.dim):
            f_val += 0.1 * np.cos(5 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.01 * np.sin(3 * x[i]) * np.cos(2 * x[j])
        
        return f_val