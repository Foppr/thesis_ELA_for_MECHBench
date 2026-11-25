import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with polynomial penalty
        r_squared = np.sum(x_scaled**2)
        radial_penalty = 0.1 * r_squared**2
        
        # Sinusoidal waves in each dimension
        wave_terms = np.sum(np.sin(3.0 * x_scaled) * np.cos(2.0 * x_scaled))
        
        # Cross-dimension interactions with polynomial coupling
        cross_terms = np.sum(x_scaled[:-1] * x_scaled[1:]) if self.dim > 1 else 0
        
        # Additional high-frequency oscillation modulated by distance from origin
        freq_mod = np.sin(15.0 * np.sqrt(r_squared)) if r_squared > 0 else 0
        
        # Combine all components with different weights
        result = 2.0 + wave_terms - radial_penalty + 0.5 * cross_terms + 0.3 * freq_mod
        
        return result