import numpy as np

class SinusoidalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create sinusoidal grid pattern with multiple local minima
        result = 0.0
        for i in range(self.dim):
            # Add multiple sinusoidal components
            result += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            # Add quadratic term for conditioning
            result += 0.1 * x_norm[i]**2
            # Add interaction terms between dimensions
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Add a global minimum at the origin
        result += 0.5 * np.sum(x_norm**2)
        
        return result