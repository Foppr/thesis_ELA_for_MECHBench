import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Global minimum at origin (0,0,...,0) with value 0
        # Multiple local minima scattered around the search space
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add additional local minima with different scales
        for i in range(self.dim):
            f_val += 0.05 * np.sin(10 * x[i])**2
        
        # Add a small noise term to make it more challenging
        f_val += 0.01 * np.random.random()
        
        return f_val