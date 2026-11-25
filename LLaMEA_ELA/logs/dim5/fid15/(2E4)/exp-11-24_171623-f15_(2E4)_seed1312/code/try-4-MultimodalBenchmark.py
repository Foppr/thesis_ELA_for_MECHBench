import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term to guide optimization towards origin
        quadratic = np.sum(x_scaled**2)
        
        # Periodic terms with varying frequencies to create multiple local minima
        periodic = np.sum(np.sin(10 * np.pi * x_scaled) ** 2 + 
                         0.5 * np.sin(20 * np.pi * x_scaled) ** 2)
        
        # Exponential interaction term to create complex curvature
        exponential = np.exp(-np.sum(x_scaled**2) / 2.0) * np.sum(np.cos(3 * x_scaled)**2)
        
        # Add a sigmoid-like penalty for large values to encourage convergence
        penalty = 1.0 / (1.0 + np.exp(-np.sum(x_scaled**2) + 2.0))
        
        # Combine all terms with different weights
        result = 0.4 * quadratic + 0.4 * periodic + 0.15 * exponential + 0.05 * penalty
        
        return result