import numpy as np

class RingOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.radial_freq = 2.0 + dim * 0.1
        self.oscillation_freq = 3.0 + dim * 0.05
        self.cross_dim_strength = 0.5 + dim * 0.02
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with periodic oscillations
        r = np.sqrt(np.sum(x**2))
        radial_term = (r - 3.0)**2 * np.cos(self.radial_freq * r) + 0.5 * np.sin(2.0 * r)
        
        # Angular oscillations in the plane
        if self.dim >= 2:
            angle = np.arctan2(x[1], x[0])
            angular_term = np.sin(self.oscillation_freq * angle) * np.cos(self.oscillation_freq * angle)
        else:
            angular_term = 0.0
            
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_term += np.sin(self.cross_dim_strength * diff) * np.cos(self.cross_dim_strength * diff)
        
        # Ring-like structure with multiple local minima
        ring_term = 0.0
        for i in range(self.dim):
            ring_term += (x[i]**2 - 4.0)**2 * np.sin(0.5 * x[i]) + 0.3 * np.cos(3.0 * x[i])
            
        # Additional periodic modulation based on all dimensions
        periodic_mod = 0.0
        for i in range(self.dim):
            periodic_mod += np.sin(self.oscillation_freq * x[i] + 0.5 * np.cos(self.oscillation_freq * x[i]))
            
        # Combine all components with different weights
        return radial_term + 0.8 * angular_term + 0.6 * cross_term + 1.2 * ring_term + 0.4 * periodic_mod