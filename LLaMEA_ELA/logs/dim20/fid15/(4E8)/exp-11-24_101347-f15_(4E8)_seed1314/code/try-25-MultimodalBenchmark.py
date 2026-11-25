import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with varying frequencies to create multiple local minima
        f2 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Product term with higher frequency to increase landscape complexity
        f3 = np.prod(np.sin(1.5 * np.pi * x_norm) * np.cos(0.7 * np.pi * x_norm))
        
        # Additional interaction term between dimensions to create correlated local optima
        f4 = 0.15 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Cross-dimensional coupling with non-linear interaction
        f5 = 0.2 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * (x_norm**3))
        
        # Adaptive scaling term to increase conditioning difficulty
        f6 = 0.1 * np.sum((x_norm**4) * np.sin(5 * np.pi * x_norm))
        
        # Combine terms with different weights
        result = f1 + f2 + 0.35 * f3 + f4 + f5 + f6
        
        return result