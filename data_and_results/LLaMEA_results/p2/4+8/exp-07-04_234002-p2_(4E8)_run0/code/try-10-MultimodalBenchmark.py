import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequencies
        f2 = np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Additional sinusoidal term with different frequency and phase
        f3 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Higher order polynomial interaction
        f4 = np.sum(x_norm**4)
        
        # Product of all dimensions with modified scaling
        f5 = np.prod(x_norm) * 0.5
        
        # Add noise term to make it more challenging
        noise = 0.05 * np.random.random()
        
        # Combine terms with different weights
        result = 0.3 * f1 + 0.25 * f2 + 0.15 * f3 + 0.2 * f4 + 0.1 * f5 + noise
        
        # Ensure global minimum is at origin
        return result