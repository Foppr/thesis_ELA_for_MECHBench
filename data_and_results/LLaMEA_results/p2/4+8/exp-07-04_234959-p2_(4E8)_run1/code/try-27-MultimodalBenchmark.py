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
        f2 = np.sum(np.sin(7.0 * x))
        
        # Sum of cosine terms with additional interactions
        f3 = np.sum(np.cos(3.0 * x))
        
        # Sum of exponential terms with different scales
        f4 = np.sum(np.exp(-0.15 * x**2))
        
        # Additional radial penalty term
        r = np.sqrt(np.sum(x**2))
        penalty = 0.1 * r**2
        
        # Combine terms with different weights to create a challenging landscape
        return 0.1 * f1 + 0.25 * f2 + 0.25 * f3 + 0.35 * f4 + penalty