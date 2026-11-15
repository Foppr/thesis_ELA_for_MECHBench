import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with mixed frequencies
        for i in range(self.dim):
            f_val += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Add cross-terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(x[i] + x[j]) * np.cos(2 * x[i] - x[j])
        
        # Add a global minimum at the origin with a modified penalty
        f_val += 0.02 * np.sum(x**4)
        
        return f_val