import numpy as np

class AdaptiveChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial base with adaptive exponents
        exponents = 2 + 2 * np.sin(np.arange(self.dim) * 0.5)
        poly_term = np.sum(np.abs(x_norm)**exponents)
        
        # Trigonometric components with dynamic frequencies
        freqs = 2 * np.pi * (1 + 0.5 * np.sin(np.arange(self.dim) * 0.3))
        trig_term = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Radial basis function component with adaptive centers
        centers = np.sin(np.arange(self.dim) * 0.7)
        rbf_term = np.sum(np.exp(-np.sum((x_norm[:, np.newaxis] - centers)**2, axis=0)))
        
        # Adaptive coupling between dimensions
        coupling = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Dynamic frequency modulation
        mod_freq = 1 + 0.3 * np.sin(np.sum(x_norm**2))
        mod_term = np.sum(np.sin(mod_freq * x_norm) * np.cos(mod_freq * x_norm))
        
        # Multi-scale oscillation with amplitude decay
        scales = np.arange(1, self.dim + 1) * 0.5
        multi_scale = np.sum(np.sin(scales * x_norm) * np.exp(-0.05 * scales))
        
        # Asymmetric penalty with exponential scaling
        asym_penalty = np.sum(np.exp(2 * np.abs(x_norm)) - 2 * x_norm**2)
        
        # Condition number varying component
        cond_factor = 1 + 0.5 * np.sin(np.sum(x_norm**4))
        cond_term = cond_factor * np.sum(x_norm**2)
        
        # Fractional dimensionality effect
        frac_dim = 0.5 + 0.5 * np.sin(np.sum(x_norm))
        frac_term = frac_dim * np.sum(np.abs(x_norm)**1.5)
        
        # Cross-dimensional interaction with varying strength
        strength = 0.3 + 0.2 * np.cos(np.arange(self.dim) * 0.4)
        cross_term = np.sum(strength * x_norm[:-1] * x_norm[1:])
        
        # Final hybrid combination
        return (poly_term + trig_term + rbf_term + coupling + mod_term + 
                multi_scale + asym_penalty + cond_term + frac_term + cross_term)