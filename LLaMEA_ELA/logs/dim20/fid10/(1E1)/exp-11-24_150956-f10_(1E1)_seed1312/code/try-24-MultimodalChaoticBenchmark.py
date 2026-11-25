import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple peaks
        radial_term = np.sum(np.exp(-5.0 * (x_scaled**2 + 0.5 * x_scaled**4)))
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled) + 
                         0.5 * np.sin(15 * x_scaled**2) * np.cos(12 * x_scaled**2))
        
        # Cross-dimensional interaction terms
        cross_term = np.sum((x_scaled[:-1] - x_scaled[1:])**2 * 
                           (np.sin(x_scaled[:-1] + x_scaled[1:]) + 1.0))
        
        # Polynomial mixture with different degrees
        poly_term = np.sum(0.8 * x_scaled**6 + 0.3 * x_scaled**4 + 0.1 * x_scaled**2)
        
        # Chaotic modulation using logistic map-like behavior
        chaotic_mod = np.sum(np.sin(np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) * 
                            np.exp(-x_scaled**2))
        
        # Combine all terms with different weights
        return 0.3 * radial_term + 0.25 * sin_term + 0.2 * cross_term + 0.15 * poly_term + 0.1 * chaotic_mod + 1.5