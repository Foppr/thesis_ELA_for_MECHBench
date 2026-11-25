import numpy as np

class ChaoticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle term with exponential decay
        chaotic_term = np.exp(-np.sum(x_norm**2) / 2) * np.sin(3 * np.pi * np.sum(x_norm**2))
        
        # Polynomial skewness component with varying degrees
        skew_term = np.sum((x_norm**5) * np.cos(2 * np.pi * x_norm))
        
        # Exponential interaction between dimensions
        exp_interaction = np.exp(-0.5 * np.sum((x_norm[:-1] - x_norm[1:])**2))
        
        # Cross-dimensional coupling with sinusoidal modulation
        coupling_term = np.sum(np.sin(5 * np.pi * x_norm[:-1]) * x_norm[1:])
        
        # Central repulsion term to create multiple local minima
        repulsion_term = 2.0 * np.exp(-np.sum((x_norm + 0.3)**2) / (2 * 0.3**2))
        
        # Combine all terms
        return chaotic_term + skew_term + exp_interaction + coupling_term + repulsion_term