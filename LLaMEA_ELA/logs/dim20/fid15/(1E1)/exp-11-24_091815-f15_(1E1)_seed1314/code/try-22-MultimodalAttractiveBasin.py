import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, significantly shifted and scaled
        basin_term = -np.exp(-np.sum((x_norm - 0.4)**2) / (2 * 0.3**2)) * 1.5
        
        # Chaotic sinusoidal oscillations with irregular frequencies per dimension
        freqs = np.linspace(5, 15, self.dim)
        oscillation_term = np.sum(np.sin(freqs * x_norm) ** 4)
        
        # Asymmetric multimodal component with different exponents and shifts
        asym_term = np.sum(((x_norm + 0.2)**4) * np.cos(3 * np.pi * x_norm)**2)
        
        # Strong cross-dimensional interaction with exponential coupling
        cross_term = np.sum(np.exp(np.abs(x_norm[:-1] - x_norm[1:])) - 1)
        
        # Additional chaotic ridge term to increase search difficulty
        ridge_term = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm)**3)
        
        # Combine all terms with varying weights for increased complexity
        return basin_term + oscillation_term + asym_term + cross_term + ridge_term