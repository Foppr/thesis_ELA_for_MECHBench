import numpy as np

class SinusoidalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = (x - self.bounds.lb) / (self.bounds.ub - self.bounds.lb) * 2 - 1
        
        # Create a multimodal landscape with sinusoidal components
        result = np.sum(x_norm**2) + 0.1 * np.sum(np.sin(5 * np.pi * x_norm))
        
        # Add additional multimodal terms
        for i in range(self.dim):
            result += 0.05 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[(i+1) % self.dim])
            
        return result