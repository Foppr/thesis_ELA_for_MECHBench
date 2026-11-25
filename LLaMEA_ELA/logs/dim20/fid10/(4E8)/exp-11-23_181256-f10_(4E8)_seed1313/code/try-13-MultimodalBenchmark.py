import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic_term = np.sum(x_norm**2)
        
        # Highly oscillatory sinusoidal terms with exponential scaling
        sinusoidal_term = np.sum(np.sin(10 * np.pi * x_norm) * np.exp(-x_norm**2))
        
        # Polynomial interaction terms creating complex landscape
        polynomial_term = np.sum((x_norm**4 - 2*x_norm**2 + 1)**2)
        
        # Mixed exponential and trigonometric term
        mixed_term = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with different weights
        result = quadratic_term + 0.2 * sinusoidal_term + 0.1 * polynomial_term - 0.03 * mixed_term
        
        return result