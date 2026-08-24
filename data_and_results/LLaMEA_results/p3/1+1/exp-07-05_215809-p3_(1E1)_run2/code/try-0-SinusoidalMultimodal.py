import numpy as np

class SinusoidalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Compute sinusoidal components
        f = 0.0
        for i in range(self.dim):
            f += np.sin(x_norm[i]) * np.cos(2 * x_norm[i]) + 0.1 * x_norm[i]**2
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.05 * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                
        # Add global minimum at origin
        f += 0.5 * np.sum(x**2)
        
        return f