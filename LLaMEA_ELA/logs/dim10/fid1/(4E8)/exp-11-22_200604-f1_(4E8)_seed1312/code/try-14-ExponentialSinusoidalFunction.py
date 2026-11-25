import numpy as np

class ExponentialSinusoidalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_norm**2)
        
        # Add sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 2.0 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
            
        # Add exponential decay terms that create complex basins
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-2.0 * np.abs(x_norm[i])) * np.sin(4 * np.pi * x_norm[i])
            
        # Add interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.3 * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
                
        # Add a global scaling factor to increase complexity
        f_val *= (1.0 + 0.1 * np.sum(np.abs(x_norm)))
        
        return f_val