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
        product_term = np.prod(np.cos(2 * x_norm))
        
        # Additional oscillatory term with frequency shift
        oscillation = np.sum(np.sin(3 * x_norm**2) * np.exp(-0.1 * x_norm**2))
        
        # Add a shifted sinusoidal component for more complex landscape
        shifted_sine = np.sum(np.sin(x_norm + 0.5) * np.cos(2 * x_norm))
        
        # Combine terms to create multimodal landscape
        return sum_squares + 0.15 * product_term + 0.02 * oscillation + 0.05 * shifted_sine