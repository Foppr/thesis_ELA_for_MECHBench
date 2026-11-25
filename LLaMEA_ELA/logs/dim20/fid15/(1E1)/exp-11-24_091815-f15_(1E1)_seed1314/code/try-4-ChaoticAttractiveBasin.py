import numpy as np

class ChaoticAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = -np.exp(-r**2 / (2 * 0.3**2)) * np.cos(2 * np.pi * r)
        
        # Multi-dimensional trigonometric wave pattern
        wave_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Chaotic component using sine of squared coordinates
        chaotic_term = np.sum(np.sin(x_norm**2) * np.exp(-x_norm**2))
        
        # Cross-term interaction between dimensions
        cross_term = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Combine all terms with different weights
        return radial_term + 0.5 * wave_term + 0.3 * chaotic_term + 0.2 * cross_term