import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_sum = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components creating multiple local minima
        sin_sum = np.sum(np.sin(3 * np.pi * x_normalized)**2)
        
        # Additional cosine terms for increased complexity
        cos_sum = np.sum(np.cos(2 * np.pi * x_normalized)**2)
        
        # Cubic term for additional curvature
        cubic_term = np.sum(x_normalized**3)
        
        # Exponential decay term to create varied landscape
        exp_term = np.sum(np.exp(-x_normalized**2))
        
        # Combine all terms with different weights
        result = quadratic_sum + 0.15 * sin_sum + 0.1 * cos_sum + 0.02 * cubic_term - 0.05 * exp_term
        
        return result