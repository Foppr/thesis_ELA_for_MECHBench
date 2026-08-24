import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_squares = np.sum(x_norm**2)
        
        # Product term with multiple local minima
        product_term = np.prod(np.cos(x_norm))
        
        # Additional oscillatory term
        oscillation = np.sum(np.sin(x_norm**2))
        
        # Combine terms to create multimodal landscape
        return sum_squares + 0.1 * product_term + 0.01 * oscillation