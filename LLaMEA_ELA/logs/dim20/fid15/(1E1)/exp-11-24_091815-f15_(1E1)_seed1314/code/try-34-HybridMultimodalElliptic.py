import numpy as np

class HybridMultimodalElliptic:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # High-conditioned elliptic term (condition number ~1e6)
        elliptic = np.sum((x_norm ** 2) * np.arange(1, self.dim + 1))
        
        # Periodic multimodal component with varying frequencies
        periodic = np.sum(np.sin(5 * np.pi * x_norm) ** 2 + 
                         0.5 * np.sin(3 * np.pi * x_norm) ** 2)
        
        # Asymmetric saddle region in the center
        saddle = -0.3 * np.sum(x_norm ** 2) + 0.1 * np.sum(x_norm ** 4)
        
        # Cross-dimensional interaction with exponentially decaying weights
        cross = np.sum(np.exp(-np.arange(1, self.dim)) * 
                      x_norm[:-1] * x_norm[1:])
        
        # Add a global shift to increase difficulty
        shift = 0.2 * np.sum(np.abs(x_norm))
        
        return elliptic + periodic + saddle + cross + shift