import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Global minimum at origin (0,0,...,0) with value 0
        # Multiple local minima scattered throughout the domain
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add more complex local optima
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
        
        return f_val