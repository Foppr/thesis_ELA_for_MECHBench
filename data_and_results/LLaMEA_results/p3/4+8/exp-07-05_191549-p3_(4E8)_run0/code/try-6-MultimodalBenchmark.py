import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add a challenging landscape with multiple peaks
        for i in range(self.dim):
            f_val += 0.05 * np.sin(10 * x[i])**2
        
        return f_val