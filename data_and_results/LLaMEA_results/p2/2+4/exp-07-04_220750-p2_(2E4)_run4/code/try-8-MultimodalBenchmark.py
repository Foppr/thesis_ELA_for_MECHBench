import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multiple sinusoidal components with different frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x_norm)) + np.sum(np.sin(4 * np.pi * x_norm)) + np.sum(np.sin(6 * np.pi * x_norm))
        
        # Quadratic penalty for being far from origin
        quad_penalty = np.sum(x_norm**2)
        
        # Exponential decay term creating multiple local minima
        exp_term = np.sum(np.exp(-x_norm**2) * np.cos(2 * np.pi * x_norm))
        
        # Cross-term creating complex interactions
        cross_term = np.sum(x_norm[:-1] * x_norm[1:]) if self.dim > 1 else 0
        
        # Combine all terms
        return sin_term + 0.5 * quad_penalty + 0.1 * exp_term + 0.05 * cross_term