import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, significantly shifted and with sharper curvature
        basin_term = -np.exp(-np.sum((x_norm - 0.4)**2) / (2 * 0.2**2)) * 1.5
        
        # Multi-frequency sinusoidal oscillations with chaotic modulation
        freqs = np.arange(1, self.dim + 1) * 3.0
        oscillation_term = np.sum(np.sin(freqs * x_norm) ** 4)
        
        # High-order multimodal component with exponential growth
        multi_term = np.sum((x_norm**5) * np.cos(6 * np.pi * x_norm)**3)
        
        # Cross-dimensional interaction with non-linear coupling
        cross_term = 0.8 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) ** 2)
        
        # Additional chaotic landscape component using logistic map-like behavior
        chaotic_term = np.sum(np.sin(10 * np.pi * np.sin(x_norm))**2)
        
        # Combine all terms with varying weights to increase conditioning
        return basin_term + oscillation_term + multi_term + cross_term + chaotic_term