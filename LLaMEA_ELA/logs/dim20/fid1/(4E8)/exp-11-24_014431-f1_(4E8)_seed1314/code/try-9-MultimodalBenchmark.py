import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic component with exponential decay
        for i in range(self.dim):
            xi = x[i]
            # Exponential decay term with sinusoidal modulation
            f_val += np.exp(-0.1 * np.abs(xi)) * np.sin(2 * np.pi * xi) ** 2
            
        # Add multiple local minima using cosine terms
        for i in range(self.dim):
            xi = x[i]
            f_val += 0.5 * np.cos(10 * xi) * np.exp(-0.05 * xi**2)
            
        # Add a global scaling factor and noise term
        f_val *= (1.0 + 0.1 * np.random.rand())
        
        # Add penalty for large values to encourage convergence
        f_val += 0.02 * np.sum(np.abs(x)**3)
        
        return f_val