import numpy as np

class HybridConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical region with quadratic basins
        spherical_term = np.sum(x_norm**2)
        
        # Elliptic structure with varying axis ratios
        elliptic_term = np.sum((x_norm**2) * (1 + 0.5 * np.sin(3 * x_norm)))
        
        # Saddle point regions with hyperbolic tangents
        saddle_term = np.sum(np.tanh(x_norm) * np.sin(2 * x_norm))
        
        # Dynamic noise injection with amplitude modulation
        noise_amplitude = 0.1 * (1 + 0.5 * np.sin(0.5 * np.sum(x_norm**2)))
        noise = noise_amplitude * np.random.normal(0, 1, self.dim)
        noise_term = np.sum(noise**2)
        
        # Cross-dimensional interaction with cosine correlations
        cross_dim = np.sum(np.cos(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                          (1 + 0.3 * np.sin(4 * x_norm[:-1]) * np.cos(2 * x_norm[1:])))
        
        # Multi-scale periodic modulation
        periodic_mod = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                             (1 + 0.2 * np.sin(5 * x_norm)) * 
                             (1 + 0.15 * np.cos(3 * x_norm)))
        
        # Asymmetric conditioning with exponential scaling
        asym_conditioning = np.sum(np.exp(0.5 * x_norm) * (1 + 0.4 * np.sin(7 * x_norm)))
        
        # Combined landscape with adaptive weights
        return 0.8 * spherical_term + 1.2 * elliptic_term + 0.6 * saddle_term + \
               0.3 * noise_term + 0.9 * cross_dim + 1.1 * periodic_mod + 0.7 * asym_conditioning