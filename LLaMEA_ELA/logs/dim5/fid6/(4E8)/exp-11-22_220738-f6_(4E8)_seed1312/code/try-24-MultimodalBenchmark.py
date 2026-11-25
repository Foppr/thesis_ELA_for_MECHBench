import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_val = np.sum(x**2)
        
        # Add multiple local minima using enhanced sine waves with varying frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add a more complex saddle point structure with cross-terms
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.1 * (x[i]**2 - x[i+1]**2) * (1 + 0.1 * np.sin(2 * x[i] * x[i+1]))
            
        # Add a conditioning factor to increase problem difficulty
        conditioning = np.sum(np.abs(x)**1.5)
        f_val += 0.05 * conditioning
        
        return f_val