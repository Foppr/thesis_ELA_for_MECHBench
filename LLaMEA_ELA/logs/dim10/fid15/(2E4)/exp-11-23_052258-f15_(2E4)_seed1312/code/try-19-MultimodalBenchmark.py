import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Sum of sinusoidal terms with higher frequency for increased complexity
        f2 = 0.5 * np.sum(np.sin(15.0 * x))
        
        # Additional cubic terms for more complex landscape
        f3 = 0.1 * np.sum(x**3)
        
        # Add interaction terms between dimensions with different weights
        f4 = 0.15 * np.sum(x[:-1] * x[1:])
        
        # New hybrid polynomial-sinusoidal component
        f5 = 0.2 * np.sum((x**4) * np.sin(8.0 * x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5