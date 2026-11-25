import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Central repulsive basin term (global optimum at origin)
        basin_term = np.exp(-np.sum(x_norm**2) / (2 * 0.3**2))
        
        # Sinusoidal oscillations with exponentially decaying amplitudes
        freqs = np.arange(1, self.dim + 1)
        oscillation_term = np.sum(np.exp(-freqs * 0.1) * np.sin(freqs * np.pi * x_norm)**2)
        
        # Cross-dimensional interaction term
        cross_term = np.sum((x_norm[:-1] - x_norm[1:])**2 * np.sin(5 * np.pi * (x_norm[:-1] + x_norm[1:]))**2)
        
        # Additional multimodal component with varying frequencies and amplitudes
        multi_term = np.sum(np.sin(7 * np.pi * x_norm) ** 4 + 0.5 * np.cos(4 * np.pi * x_norm)**3)
        
        # Combine all terms
        return basin_term + oscillation_term + cross_term + multi_term