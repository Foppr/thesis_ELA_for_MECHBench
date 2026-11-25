import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal perturbations
        f2 = 0.1 * np.sum(np.sin(5.0 * x))
        
        # Add a cubic term to create more complex landscape
        f3 = 0.01 * np.sum(x**3)
        
        # Combine all terms with different weights
        result = f1 + f2 + f3
        
        return result