import numpy as np

class ChaoticSaddleValley:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial valley terms with varying degrees and offsets
        valley_terms = np.sum((x_norm**2 + 0.1 * x_norm**4 + 0.01 * x_norm**6) * np.exp(-0.5 * (x_norm**2)))
        
        # Chaotic saddle point component using logistic map-inspired nonlinearity
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i])
        
        # Gradient discontinuity term using sign and step functions
        discont_term = np.sum(np.abs(x_norm) ** 1.5)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-np.abs(x_norm[i] - x_norm[i+1])) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Combine all components with different weights to balance challenge aspects
        return 0.5 * valley_terms + 0.3 * chaotic_term + 0.2 * discont_term + 0.1 * cross_coupling