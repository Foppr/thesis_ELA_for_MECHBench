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
        f2 = 0.2 * np.sum(np.sin(10 * np.pi * x_norm))
        
        # Add a global scaling factor and offset for better conditioning
        # Introduce cubic interaction terms for increased complexity
        f3 = 0.03 * np.sum(x_norm**3)
        
        # Add cross-terms to increase interaction between dimensions
        cross_terms = 0.015 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Add quartic terms for enhanced landscape complexity
        f4 = 0.02 * np.sum(x_norm**4)
        
        return f1 + f2 + f3 + cross_terms + f4