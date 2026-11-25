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
        
        # Add sinusoidal multimodal components
        result += 0.5 * np.sum(np.sin(5 * np.pi * x_norm))
        
        # Add higher-order polynomial terms for increased complexity
        result += 0.1 * np.sum(x_norm**4)
        
        # Add cross-dimensional sinusoidal interactions
        for i in range(self.dim):
            result += 0.2 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[(i+1) % self.dim])
            
        # Add mixed polynomial and sinusoidal terms
        for i in range(self.dim):
            result += 0.05 * (x_norm[i]**3) * np.sin(4 * np.pi * x_norm[(i+2) % self.dim])
            
        return result