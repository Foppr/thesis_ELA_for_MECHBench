import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with different degrees
        f1 = np.sum(x**4)
        
        # Trigonometric terms with varying frequencies
        f2 = np.sum(np.cos(3.0 * x) * np.sin(2.0 * x))
        
        # Logarithmic terms with offset to avoid singularity
        f3 = np.sum(np.log(np.abs(x) + 1.0))
        
        # Exponential decay terms
        f4 = np.sum(np.exp(-0.5 * x**2))
        
        # Combine all terms with different weights
        return 0.2 * f1 + 0.3 * f2 + 0.25 * f3 + 0.25 * f4