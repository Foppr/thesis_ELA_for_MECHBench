import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for sinusoidal components
        x_norm = (x - self.bounds.lb) / (self.bounds.ub - self.bounds.lb) * 2 - 1
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add sinusoidal modulation with multiple peaks
        for i in range(self.dim):
            f_val += 0.5 * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(np.pi * (x[i] + x[j])) * np.cos(0.5 * np.pi * (x[i] - x[j]))
        
        # Add global minimum at origin with additional complexity
        f_val += 0.3 * np.sum(np.sin(5 * x)**2)
        
        return f_val