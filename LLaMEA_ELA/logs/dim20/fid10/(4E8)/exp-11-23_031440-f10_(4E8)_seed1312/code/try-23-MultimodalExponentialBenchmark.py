import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms that create steep gradients
        exp_term = np.sum(np.exp(-5.0 * np.abs(x_norm)) * (1.0 - np.exp(-2.0 * np.abs(x_norm))))
        
        # Polynomial interaction terms to create complex landscape
        poly_interaction = 0.5 * np.sum(x_norm**4) + 0.3 * np.sum(x_norm**6)
        
        # Add sinusoidal modulation to create multiple local minima
        sin_modulation = 0.2 * np.sum(np.sin(10 * x_norm) ** 2)
        
        # Create widely separated global minima using distance-based penalty
        # Global minima at positions that are multiples of 0.8
        grid_positions = np.arange(-1, 1.1, 0.8)
        distances = np.zeros_like(x_norm)
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - grid_positions))
            distances[i] = min_dist
        
        # Penalty term to attract solutions towards global minima
        global_min_penalty = 5.0 * np.sum(distances**3)
        
        # Combine all terms with different weights
        result = exp_term + poly_interaction + sin_modulation + global_min_penalty
        
        return result