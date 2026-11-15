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
        
        # Product term with multiple local minima and chaotic interference
        product_term = np.prod(np.cos(10 * x_norm))
        
        # Additional oscillatory term with varying frequencies
        oscillation = np.sum(np.sin(100 * x_norm**2))
        
        # Rugged terrain term with multiple peaks and valleys
        rugged = np.sum(np.abs(x_norm) * np.sin(50 * np.abs(x_norm)))
        
        # Chaotic modulation term
        chaotic = np.sum(np.sin(np.exp(x_norm)) * np.cos(np.log(np.abs(x_norm) + 1e-10)))
        
        # Combine all terms to create a highly multimodal landscape
        return sum_squares + 0.5 * product_term + 0.05 * oscillation + 0.3 * rugged + 0.2 * chaotic