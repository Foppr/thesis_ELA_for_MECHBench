import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term
        basin_term = -np.exp(-np.sum(x_norm**2) / (2 * 0.5**2))
        
        # Sinusoidal oscillations in each dimension
        oscillation_term = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Additional multimodal component with varying frequencies
        multi_term = np.sum((x_norm**2) * np.sin(3 * np.pi * x_norm)**2)
        
        # Combine all terms
        return basin_term + oscillation_term + multi_term