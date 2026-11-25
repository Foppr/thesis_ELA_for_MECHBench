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
        
        # Add enhanced sinusoidal modulation with multiple peaks and varying frequencies
        for i in range(self.dim):
            f_val += 0.8 * np.sin(4 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Add interaction terms between dimensions with higher complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(2 * np.pi * (x[i] + x[j])) * np.cos(np.pi * (x[i] - x[j]))
        
        # Add global minimum at origin with additional complexity and higher frequency components
        f_val += 0.5 * np.sum(np.sin(7 * x)**2)
        
        # Add a challenging plateau region by incorporating a sigmoid-like term
        f_val += 0.1 * np.sum(1 / (1 + np.exp(-x**2)))
        
        return f_val