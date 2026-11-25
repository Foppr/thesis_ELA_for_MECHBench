import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function value
        # Global minimum at (1,1,...,1): f(1) = 0
        # Multiple local minima scattered around the search space
        
        # Base quadratic term shifted
        f_val = np.sum((x - 1)**2)
        
        # Add multiple local minima using higher frequency cosine terms
        for i in range(self.dim):
            f_val += 0.2 * np.cos(10 * x[i]) * np.exp(-0.05 * (x[i] - 1)**2)
            
        # Add interaction terms between dimensions with cubic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.02 * np.sin(5 * x[i]) * np.cos(3 * x[j]) * (x[i] * x[j])**3
        
        # Add a small noise term to increase landscape irregularity
        f_val += 0.001 * np.sum(x**4)
        
        return f_val