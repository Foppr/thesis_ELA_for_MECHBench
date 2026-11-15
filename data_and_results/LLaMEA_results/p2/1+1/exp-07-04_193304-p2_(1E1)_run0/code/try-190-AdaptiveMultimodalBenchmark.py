import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency factors for dynamic modulation
        self.freq_factors = np.arange(1, dim + 1) * np.pi * 0.8
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial base with adaptive exponents
        exponents = 2 + 2 * np.sin(np.arange(self.dim) * 0.5)
        poly_term = np.sum(np.abs(x_norm)**exponents)
        
        # Trigonometric components with dynamic frequencies
        trig_term = np.sum(np.sin(self.freq_factors * x_norm) * np.cos(self.freq_factors * x_norm))
        
        # Radial basis function component with adaptive centers
        centers = np.sin(np.arange(self.dim) * 0.3) * 0.5
        rbf_term = np.sum(np.exp(-0.5 * np.sum((x_norm[:, np.newaxis] - centers)**2, axis=0)))
        
        # Cross-dimensional coupling with sine modulation
        coupling_term = 0.5 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                                   np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Adaptive scaling based on dimensionality
        dim_factor = np.log(self.dim + 1) / np.log(10)
        
        # Dynamic frequency modulation
        mod_freq = self.freq_factors * (1 + 0.3 * np.sin(x_norm))
        mod_term = np.sum(np.sin(mod_freq * x_norm) * np.cos(mod_freq * x_norm))
        
        # Multi-scale oscillation
        scale_term = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm) * 
                           np.exp(-0.2 * x_norm**2))
        
        # Asymmetric penalty
        asym_term = np.sum(np.abs(x_norm)**3 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Combined fitness
        return dim_factor * (poly_term + trig_term + rbf_term + coupling_term + 
                           mod_term + scale_term + asym_term)