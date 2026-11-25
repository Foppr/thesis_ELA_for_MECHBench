import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, significantly shifted and shaped
        basin_term = -np.exp(-np.sum((x_norm - 0.3)**2) / (2 * 0.3**2))
        
        # Chaotic sinusoidal oscillations with varying frequencies and amplitudes
        oscillation_term = np.sum(np.sin(11 * np.pi * x_norm) ** 4 + 0.5 * np.sin(17 * np.pi * x_norm) ** 2)
        
        # Enhanced multimodal component with chaotic polynomial interactions
        multi_term = np.sum((x_norm**5) * np.sin(5 * np.pi * x_norm)**3)
        
        # Saddle point inducing cross-dimensional interaction term
        cross_term = 0.7 * np.sum(x_norm[:-1] ** 2 * x_norm[1:] ** 2)
        
        # Additional non-separable chaotic interaction
        chaotic_term = 0.3 * np.sum(np.sin(np.pi * x_norm[:-1] * x_norm[1:]) ** 2)
        
        # Combine all terms with increased complexity
        return basin_term + oscillation_term + multi_term + cross_term + chaotic_term