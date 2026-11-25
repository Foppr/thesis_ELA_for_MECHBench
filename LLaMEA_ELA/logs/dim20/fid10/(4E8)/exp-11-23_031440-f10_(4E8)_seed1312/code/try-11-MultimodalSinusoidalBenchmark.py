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
        
        # Enhanced sinusoidal modulation with multiple frequencies
        for i in range(self.dim):
            f_val += 0.8 * np.sin(4 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Stronger interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(2 * np.pi * (x[i] + x[j])) * np.cos(np.pi * (x[i] - x[j]))
        
        # Additional complex sinusoidal pattern with global minimum enhancement
        f_val += 0.5 * np.sum(np.sin(7 * x)**2)
        
        # Add a more challenging landscape component with varying amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(6 * np.pi * x[i]) * np.cos(4 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        return f_val