import numpy as np

class SinusoidalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Compute sinusoidal components
        f = np.sum(np.sin(x_norm) * np.cos(2 * x_norm)) + 0.1 * np.sum(x_norm**2)
        
        # Add multiple global minima at different locations
        minima_positions = np.array([[-2.5, 2.5] * (self.dim // 2 + 1)])[:self.dim]
        minima_positions = np.tile(minima_positions, (1, 1))
        
        # Add penalty for being far from minima
        penalty = np.sum(np.minimum(np.abs(x - minima_positions), 5.0))
        
        return f + penalty