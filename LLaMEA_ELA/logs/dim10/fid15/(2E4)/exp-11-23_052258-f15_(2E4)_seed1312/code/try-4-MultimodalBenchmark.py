import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic term for global attraction
        f1 = np.sum(x**2)
        
        # Sinusoidal terms with varying frequencies and amplitudes
        f2 = np.sum(np.sin(10.0 * x) * np.cos(3.0 * x))
        
        # Higher-order polynomial terms for increased complexity
        f3 = 0.01 * np.sum(x**6)
        
        # Additional cosine term to create more local minima
        f4 = 0.5 * np.sum(np.cos(7.0 * x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4