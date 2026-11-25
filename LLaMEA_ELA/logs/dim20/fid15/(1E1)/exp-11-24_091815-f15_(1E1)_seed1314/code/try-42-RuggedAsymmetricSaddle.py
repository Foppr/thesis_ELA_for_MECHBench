import numpy as np

class RuggedAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with asymmetric weighting
        quad_term = np.sum(x_norm**2 * (1 + 0.5 * np.abs(x_norm)))
        
        # Rugged sinusoidal component with exponentially decaying amplitude
        rugged_term = np.sum(np.exp(-np.abs(x_norm)) * np.sin(3 * np.pi * x_norm)**2)
        
        # Asymmetric saddle points with varying steepness
        saddle_term = np.sum((x_norm**4 - 2 * x_norm**2) * np.exp(-0.5 * x_norm**2))
        
        # Cross-dimensional interaction with decay factor
        cross_term = 0.3 * np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Add noise-like perturbations to increase ruggedness
        noise = 0.1 * np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        return quad_term + rugged_term + saddle_term + cross_term + noise