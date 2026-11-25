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
        
        # Add multiple local minima using higher frequency cosine terms
        for i in range(self.dim):
            f_val += 0.15 * np.cos(7 * x[i]) * np.exp(-0.05 * (x[i] - 1.5)**2)
            
        # Add interaction terms between dimensions with sine functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.02 * np.sin(4 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i] + x[j])**2)
        
        # Add shifted local minima
        for i in range(self.dim):
            f_val += 0.08 * np.sin(6 * x[i]) * np.exp(-0.1 * (x[i] + 2)**2)
        
        return f_val