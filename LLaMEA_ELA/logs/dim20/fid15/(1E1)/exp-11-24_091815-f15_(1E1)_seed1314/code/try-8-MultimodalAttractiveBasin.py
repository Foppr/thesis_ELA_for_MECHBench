import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Multiple central attractive basins at different locations
        basin_term = -np.sum(np.exp(-np.sum((x_norm - np.sin(np.arange(1, self.dim + 1) * np.pi / 4))**2) / (2 * 0.3**2)))
        
        # Chaotic sinusoidal oscillations with varying frequencies and amplitudes
        oscillation_term = np.sum(np.sin(7 * np.pi * x_norm) ** 2 + 0.5 * np.sin(13 * np.pi * x_norm) ** 2)
        
        # Additional multimodal component with exponential modulation
        multi_term = np.sum(np.exp(x_norm**2) * np.sin(4 * np.pi * x_norm)**2)
        
        # Saddle point component to create flat regions and deceptive landscapes
        saddle_term = 0.3 * np.sum(x_norm * np.cos(2 * np.pi * x_norm))
        
        # Combine all terms
        return basin_term + oscillation_term + multi_term + saddle_term