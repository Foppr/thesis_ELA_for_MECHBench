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
        
        # Enhanced sinusoidal terms with higher frequencies and different phases
        f2 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Radial symmetry component with modified trigonometric interactions
        radius = np.sqrt(np.sum(x_norm**2))
        f3 = 0.2 * radius * np.sin(4 * np.pi * radius) * np.cos(2 * np.pi * radius)
        
        # Product term with higher frequency to increase landscape complexity
        f4 = np.prod(np.sin(3 * np.pi * x_norm) * np.cos(0.7 * np.pi * x_norm))
        
        # Additional interaction term between dimensions with increased weight
        f5 = 0.15 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Cross-dimensional interaction with exponential scaling
        f6 = 0.05 * np.sum(np.exp(2 * np.abs(x_norm)) * np.sin(np.pi * x_norm))
        
        # Combine terms with different weights
        result = f1 + f2 + f3 + 0.4 * f4 + f5 + f6
        
        return result