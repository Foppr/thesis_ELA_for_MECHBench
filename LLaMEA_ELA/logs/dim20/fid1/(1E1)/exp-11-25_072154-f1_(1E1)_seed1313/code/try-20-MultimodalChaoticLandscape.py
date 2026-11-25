import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Sinusoidal periodic components with varying frequencies
        sin_component = np.sum(np.sin(2 * np.pi * x_scaled) + 0.5 * np.sin(4 * np.pi * x_scaled))
        
        # Polynomial penalty terms to create valleys and ridges
        poly_penalty = np.sum(x_scaled**4 + 0.3 * x_scaled**2)
        
        # Cross-terms creating interaction between dimensions
        cross_terms = np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2))
        
        # Additional chaotic modulation using a logistic map-inspired function
        logistic_mod = np.sum(np.sin(10 * np.pi * np.abs(x_scaled)) * np.cos(7 * np.pi * np.abs(x_scaled)))
        
        # Combine all components with different weights
        return 0.3 * sin_component + 0.4 * poly_penalty + 0.2 * cross_terms + 0.1 * logistic_mod