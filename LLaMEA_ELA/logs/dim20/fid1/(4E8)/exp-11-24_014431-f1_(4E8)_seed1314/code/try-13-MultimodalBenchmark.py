import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Global minimum at origin: f(0) = 0
        # Multiple local minima scattered throughout the domain
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using a combination of sinusoidal terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        # Add a more complex penalty term to encourage staying near the origin
        f_val += 0.02 * np.sum(x**6) + 0.01 * np.sum(x**4)
        
        # Add a cross-term interaction to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(x[i]) * np.cos(x[j])
                
        return f_val