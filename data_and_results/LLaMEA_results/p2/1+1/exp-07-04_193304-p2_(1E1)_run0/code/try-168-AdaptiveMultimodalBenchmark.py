import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency factors for stability
        self.freq_factors = np.arange(1, dim + 1) * np.pi * 0.8
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial base with adaptive exponents
        exponents = 2 + np.sin(np.arange(self.dim) * 0.7) * 1.5
        poly_term = np.sum(np.abs(x_norm)**exponents)
        
        # Trigonometric components with dynamic frequencies
        trig_term = np.sum(np.sin(self.freq_factors * x_norm) * np.cos(self.freq_factors * x_norm))
        
        # Radial basis function component with adaptive centers
        centers = np.sin(np.arange(self.dim) * 0.5) * 0.5
        rbf_term = np.sum(np.exp(-np.sum((x_norm.reshape(-1, 1) - centers.reshape(1, -1))**2, axis=1) * 0.5))
        
        # Cross-dimensional coupling with dynamic weights
        coupling_weights = 0.5 + 0.5 * np.sin(np.arange(self.dim-1) * 0.3)
        coupling_term = np.sum(coupling_weights * np.sin(x_norm[:-1] * x_norm[1:]) * np.cos(x_norm[:-1] * x_norm[1:]))
        
        # Adaptive penalty based on distance from origin
        distance = np.sqrt(np.sum(x_norm**2))
        penalty_term = 0.3 * distance * np.exp(-0.1 * distance)
        
        # Multi-scale oscillation with varying amplitude
        scale_freqs = np.arange(1, self.dim + 1) * 3.2
        scale_term = np.sum(np.sin(scale_freqs * x_norm) * np.exp(-0.05 * np.abs(x_norm)))
        
        # Asymmetric exponential decay
        decay_rates = 0.1 + 0.2 * np.sin(np.arange(self.dim) * 0.4)
        exp_term = np.sum(np.exp(-decay_rates * np.abs(x_norm)) * np.sin(x_norm))
        
        # Dynamic conditioning based on dimension
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.1)
        conditioned_term = condition_factor * np.sum(x_norm**4)
        
        # Fractional dimensionality effect
        dim_effect = np.sum(np.abs(x_norm)**(1.3 + 0.4 * np.sin(np.arange(self.dim) * 0.8)))
        
        # Combined result
        return (poly_term + trig_term + rbf_term + coupling_term + 
                penalty_term + scale_term + exp_term + conditioned_term + dim_effect)