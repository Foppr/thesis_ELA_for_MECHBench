import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = 0.1 * np.sum(np.sin(5.0 * x))
        
        # Additional polynomial terms for complexity
        f3 = 0.01 * np.sum(x**4)
        
        # Combine all terms with different weights
        return f1 + f2 + f3