import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal waves with dimension-dependent frequency modulation
        freq_mod = 1.0 + 0.3 * np.sqrt(self.dim)
        sin_wave = np.sum(np.sin(freq_mod * x_norm) * np.cos(freq_mod * x_norm**2))
        
        # Polynomial repulsion terms that increase with dimensionality
        poly_repel = np.sum((x_norm**2 + 0.01)**(-2.0)) * 0.7
        
        # Adaptive scaling based on dimension
        scale_factor = 1.0 + 0.1 * self.dim
        
        # Combined function with multiple interacting components
        return scale_factor * (0.5 * sin_wave + 0.3 * poly_repel + 0.2 * np.sum(x_norm**4))