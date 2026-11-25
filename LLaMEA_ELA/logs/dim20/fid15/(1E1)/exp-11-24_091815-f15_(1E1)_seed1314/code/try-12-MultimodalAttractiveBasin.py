import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, slightly shifted
        basin_term = -np.exp(-np.sum((x_norm - 0.2)**2) / (2 * 0.3**2))
        
        # Enhanced sinusoidal oscillations with varying frequencies per dimension
        oscillation_term = np.sum(np.sin(9 * np.pi * x_norm) ** 2 + 0.5 * np.sin(15 * np.pi * x_norm) ** 2)
        
        # Additional multimodal component with higher-order nonlinearity and interaction
        multi_term = np.sum((x_norm**4) * np.cos(3 * np.pi * x_norm)**2 + 0.3 * x_norm**6)
        
        # Increased cross-dimensional interaction term to raise conditioning difficulty
        cross_term = 0.7 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(np.pi * (x_norm[:-1] + x_norm[1:]))**2)
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim)
        
        # Combine all terms with adaptive scaling
        return scale_factor * (basin_term + oscillation_term + multi_term + cross_term)