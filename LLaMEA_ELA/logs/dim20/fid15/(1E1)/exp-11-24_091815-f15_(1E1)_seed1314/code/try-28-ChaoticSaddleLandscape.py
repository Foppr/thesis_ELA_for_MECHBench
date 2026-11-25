import numpy as np

class ChaoticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Saddle point structure with multiple attracting regions
        saddle_term = np.sum(x_norm**2 * np.cos(2 * np.pi * x_norm)**2)
        
        # High-frequency oscillation creating many local minima
        oscillation_term = np.sum(np.sin(10 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay
        cross_term = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Non-convexity through polynomial interactions
        poly_term = np.sum((x_norm**4 - 2 * x_norm**2) * np.sin(np.pi * x_norm))
        
        # Combine all terms with different weights to create a challenging landscape
        return 0.5 * chaotic_term + 0.3 * saddle_term + 0.2 * oscillation_term + 0.1 * cross_term + 0.4 * poly_term