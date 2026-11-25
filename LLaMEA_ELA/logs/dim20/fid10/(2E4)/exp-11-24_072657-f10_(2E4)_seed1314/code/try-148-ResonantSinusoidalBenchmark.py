import numpy as np

class ResonantSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal gradient interactions with polynomial decay
        sinusoidal_terms = np.sum(np.sin(2.0 * np.pi * x_norm) * 
                                np.cos(3.0 * np.pi * x_norm) * 
                                (1.0 + 0.4 * x_norm**2))
        
        # Polynomial decay with adaptive scaling
        poly_decay = np.sum((1.0 + 0.3 * np.abs(x_norm))**(-2.5) * 
                           np.sin(1.5 * x_norm) * 
                           np.cos(2.0 * x_norm))
        
        # Dynamic dimensional coupling with frequency modulation
        freq_mod = 1.0 + 0.6 * np.sin(0.4 * self.dim) + 0.3 * np.cos(0.2 * self.dim)
        dynamic_terms = np.sum(np.exp(-freq_mod * np.abs(x_norm)) * 
                             np.sin(freq_mod * x_norm + 0.5 * np.sin(0.7 * x_norm)) * 
                             np.cos(freq_mod * x_norm + 0.3 * np.cos(0.9 * x_norm)))
        
        # Cross-dimensional resonance with adaptive coupling
        coupling_strength = 0.8 + 0.2 * np.sin(0.6 * self.dim)
        cross_resonance = np.sum(coupling_strength * 
                               np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                               np.sin(2.0 * (x_norm[:-1] - x_norm[1:])) * 
                               np.cos(1.5 * (x_norm[:-1] + x_norm[1:])))
        
        # Adaptive conditioning with multi-scale modulation
        conditioning_factor = 1.0 + 0.4 * np.sin(0.2 * self.dim) * np.cos(0.3 * self.dim)
        
        # Combined landscape with enhanced multi-modality
        result = (0.8 * sinusoidal_terms + 0.6 * poly_decay + 0.7 * dynamic_terms + 
                 0.5 * cross_resonance) * conditioning_factor
        
        # Add controlled noise for increased complexity
        noise = 0.002 * np.random.random() * (1.0 + 0.15 * np.sin(self.dim * 0.6))
        
        return result + noise