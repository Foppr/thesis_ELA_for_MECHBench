import numpy as np

class SinusoidalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = (x - self.bounds.lb) / (self.bounds.ub - self.bounds.lb) * 2 - 1
        
        # Base quadratic term
        result = np.sum(x_norm**2)
        
        # Enhanced sinusoidal oscillations
        result += 0.2 * np.sum(np.sin(7 * np.pi * x_norm))
        
        # Modified interaction terms with different frequencies
        for i in range(self.dim):
            result += 0.1 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[(i+1) % self.dim])
            
        # Additional high-frequency noise term
        result += 0.05 * np.sum(np.sin(10 * np.pi * x_norm**2))
            
        return result