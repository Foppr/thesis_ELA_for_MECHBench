import numpy as np

class SinusoidalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = (x - self.bounds.lb) / (self.bounds.ub - self.bounds.lb) * 2 - 1
        
        # Base quadratic term
        f_val = np.sum(x_norm**2)
        
        # Add sinusoidal modulations with different frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        return f_val