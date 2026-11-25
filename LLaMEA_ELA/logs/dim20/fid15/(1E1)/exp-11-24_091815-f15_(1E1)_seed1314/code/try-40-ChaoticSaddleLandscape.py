import numpy as np

class ChaoticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle term with exponential decay
        chaotic_term = np.sum(np.exp(-np.abs(x_norm)) * np.sin(2 * np.pi * x_norm))
        
        # Periodic attractor components with varying frequencies
        periodic_term = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm))
        
        # Exponentially decaying gradient landscape
        decay_term = np.sum(np.exp(-0.5 * x_norm**2) * (x_norm**4 - 2 * x_norm**2))
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.exp(-0.1 * np.abs(x_norm[:-1] + x_norm[1:])))
        
        # Add a small noise term to increase conditioning
        noise = 0.01 * np.sum(np.sin(10 * x_norm) ** 2)
        
        return chaotic_term + periodic_term + decay_term + cross_term + noise