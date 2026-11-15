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
            # Add multiple sinusoidal components with different frequencies
            result += np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
            # Add cubic term for increased nonlinearity
            result += 0.05 * x_norm[i]**3
            # Add interaction terms between dimensions with different frequencies
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(1.5 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2.5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Add a global minimum at the origin with modified conditioning
        result += 0.3 * np.sum(x_norm**2)
        
        return result