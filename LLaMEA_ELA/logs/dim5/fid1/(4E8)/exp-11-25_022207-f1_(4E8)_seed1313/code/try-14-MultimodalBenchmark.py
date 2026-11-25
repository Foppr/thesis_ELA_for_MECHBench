import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add sinusoidal modulation to create multiple local minima with higher frequency
        f2 = 0.15 * np.sum(np.sin(7 * np.pi * x_norm))
        
        # Add a global scaling factor and offset for better conditioning
        # Introduce quartic interaction terms for increased complexity
        f3 = 0.05 * np.sum(x_norm**4)
        
        # Add cross-terms to increase interaction between dimensions
        cross_terms = 0.02 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + f2 + f3 + cross_terms