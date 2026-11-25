import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sine waves
        for i in range(self.dim):
            f_val += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add a saddle point structure
        if self.dim >= 2:
            f_val += 0.05 * np.sum((x[:-1] - x[1:])**2)
            
        return f_val