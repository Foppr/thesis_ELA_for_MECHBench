import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees to create complex curvature
        f1 = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric terms with multiple frequencies and phases
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                   np.sin(7 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Radial component with adaptive scaling based on distance from origin
        r = np.sqrt(np.sum(x_norm**2))
        f3 = 0.5 * r * (1 + 0.3 * np.sin(10 * r))
        
        # Cross-terms between dimensions to create correlated local optima
        f4 = 0.1 * np.sum((x_norm[:-1] - 0.5 * x_norm[1:])**2)
        
        # Interaction term with exponential decay to control landscape complexity
        f5 = np.exp(-0.5 * r**2) * np.sum(np.sin(8 * np.pi * x_norm))
        
        # Combine all terms with different weights
        result = 0.8 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.4 * f5
        
        return result