import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, slightly shifted
        basin_term = -np.exp(-np.sum((x_norm - 0.3)**2) / (2 * 0.35**2))
        
        # Sinusoidal oscillations with varying frequencies per dimension
        oscillation_term = np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        
        # Additional multimodal component with higher-order nonlinearity
        multi_term = np.sum((x_norm**4) * np.sin(5 * np.pi * x_norm)**2)
        
        # Cross-dimensional interaction term to increase conditioning
        cross_term = 0.6 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all terms
        return basin_term + oscillation_term + multi_term + cross_term