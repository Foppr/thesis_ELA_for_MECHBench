import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Sum of sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(5.0 * x))
        
        # Sum of exponential terms with different scales
        f3 = np.sum(np.exp(-0.1 * x**2))
        
        # Combine terms with different weights to create a challenging landscape
        return 0.1 * f1 + 0.3 * f2 + 0.6 * f3