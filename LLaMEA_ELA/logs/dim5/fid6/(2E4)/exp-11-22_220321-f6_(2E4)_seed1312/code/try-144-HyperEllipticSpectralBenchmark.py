import numpy as np

class HyperEllipticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.spectral_decay = 0.8
        self.harmonic_amplitude = 1.5
        self.condition_number = 100.0
        self.resolution_levels = min(5, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spectral filtering component with adaptive decay
        spectral_term = 0.0
        for i in range(self.dim):
            # Apply frequency-based weighting
            freq_weight = np.exp(-self.spectral_decay * i)
            spectral_term += freq_weight * (x[i] ** 2) * (1.0 + 0.1 * np.sin(x[i] * 3.0))
        
        # Multi-resolution harmonic coupling
        harmonic_term = 0.0
        for level in range(1, self.resolution_levels + 1):
            level_weight = 1.0 / (level ** 1.5)
            level_sum = 0.0
            for i in range(self.dim):
                freq = 2.0 ** level
                level_sum += np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5)
            harmonic_term += level_weight * (level_sum ** 2)
        
        # Condition number modulation
        condition_mod = 1.0 + (self.condition_number - 1.0) * (np.sum(x**2) / (self.dim * 25.0))
        
        # Cross-dimensional coupling with elliptic geometry
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Elliptic interaction term
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                cross_term += (1.0 / (dist + 0.1)) * np.sin(x[i] * x[j])
        
        # Adaptive amplitude scaling based on dimensionality
        amp_scale = self.harmonic_amplitude * (1.0 + 0.2 * np.log(self.dim + 1))
        
        return condition_mod * (0.4 * spectral_term + 0.3 * harmonic_term + 0.3 * cross_term)