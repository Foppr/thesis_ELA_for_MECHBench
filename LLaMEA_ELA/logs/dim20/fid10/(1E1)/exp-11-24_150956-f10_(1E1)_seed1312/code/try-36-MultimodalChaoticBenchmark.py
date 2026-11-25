import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple peaks
        radial_term = np.sum((x_scaled**2 + 0.1) * np.exp(-x_scaled**2))
        
        # Sinusoidal waves with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled) + 
                         0.5 * np.sin(15 * x_scaled) * np.cos(12 * x_scaled))
        
        # Polynomial interactions with mixed degrees
        poly_term = np.sum(x_scaled**6 + 0.8 * x_scaled**4 + 0.3 * x_scaled**2)
        
        # Cross-dimensional interaction terms creating complex valleys
        cross_term = np.sum(np.sin(x_scaled[:-1] * x_scaled[1:]) * 
                           np.cos(0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Additional chaotic sine-wave component
        chaotic_term = np.sum(np.sin(3 * np.pi * x_scaled) * 
                             np.cos(2 * np.pi * x_scaled) * 
                             np.exp(-0.5 * x_scaled**2))
        
        # Combine all terms with different weights
        return 0.3 * radial_term + 0.25 * sin_term + 0.2 * poly_term + 0.15 * cross_term + 0.1 * chaotic_term