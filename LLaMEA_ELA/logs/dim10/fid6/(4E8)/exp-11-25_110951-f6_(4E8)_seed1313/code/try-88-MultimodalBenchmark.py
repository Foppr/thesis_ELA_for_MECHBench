import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Sinusoidal oscillatory component with varying frequencies
        sin_component = np.sum(np.sin(8 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        
        # Polynomial conditioning term that increases complexity with dimensionality
        poly_conditioning = np.sum((x_normalized ** 4) * (1 + 0.5 * np.sin(3 * np.pi * x_normalized)))
        
        # Radial basin term with exponential decay and sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        basin_term = -np.exp(-r**2) * np.sin(5 * np.pi * r)
        
        # Cross-dimensional interaction with coupled sine-cosine terms
        cross_interaction = 0.5 * np.sum(
            np.sin(3 * np.pi * x_normalized[:-1]) * 
            np.cos(3 * np.pi * x_normalized[1:]) * 
            (1 + 0.2 * np.sin(2 * np.pi * r))
        )
        
        # Multi-scale chaotic perturbation using nested trigonometric functions
        chaos_perturbation = 0.3 * np.sum(
            np.sin(10 * np.pi * x_normalized) * 
            np.cos(7 * np.pi * x_normalized) * 
            np.sin(5 * np.pi * r)
        )
        
        # Dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.2 * (self.dim - 1) + 0.05 * np.sin(self.dim)
        
        # Combine all components with appropriate weighting
        return scale_factor * (sin_component + poly_conditioning + basin_term + cross_interaction + chaos_perturbation)