import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Multiple local minima using trigonometric terms
        trigonometric = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Additional challenging landscape with mixed scales
        mixed = np.sum((x_norm**4 - 2 * x_norm**2 + 1) * np.exp(-0.5 * x_norm**2))
        
        # Combine all components
        return quadratic + 0.1 * trigonometric + 0.01 * mixed