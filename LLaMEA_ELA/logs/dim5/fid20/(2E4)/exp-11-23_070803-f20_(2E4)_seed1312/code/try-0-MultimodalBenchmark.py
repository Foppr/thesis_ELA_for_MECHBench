import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add polynomial terms
        for i in range(self.dim):
            f_val += x[i]**4 - 16*x[i]**2 + 5*x[i]
        
        # Add trigonometric terms for multimodality
        for i in range(self.dim):
            f_val += -2 * np.sin(2 * np.pi * x[i])
        
        # Add interaction terms between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * (x[i] - x[j])**2
        
        # Add exponential decay term to create basins
        f_val += np.exp(-0.1 * np.sum(x**2))
        
        return f_val