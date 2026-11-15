import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create a sinusoidal grid pattern with multiple local minima
        result = 0.0
        for i in range(self.dim):
            # Add a combination of sinusoidal and quadratic terms
            result += (x_norm[i] ** 2 - 2 * np.cos(2 * np.pi * x_norm[i]) + 1) * (1 + 0.1 * np.sin(3 * x_norm[i]))
        
        # Add a global scaling factor and offset
        result = result * 0.5 + 0.1 * np.sum(x_norm ** 2)
        
        return result