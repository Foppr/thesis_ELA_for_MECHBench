import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar fractal structure using recursive sine-cosine combinations
        fractal_term = np.sum(np.sin(3.0 * np.sin(2.0 * x)) * np.cos(2.0 * np.cos(1.5 * x)))
        
        # Adaptive gradient field with dimension-dependent scaling
        grad_field = np.sum((x**2 + 0.1) * np.exp(-0.5 * x**2) * np.sin(1.2 * x))
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes
        harmonic_term = np.sum(np.sin(4.0 * x) * np.cos(3.0 * x) * 
                              np.sin(2.0 * x) * np.cos(x) * 
                              (1 + 0.2 * np.sin(0.5 * x)**2))
        
        # Geometric scaling factor based on dimensionality and position
        geom_factor = np.prod(np.abs(x) + 1.0)
        
        # Cross-dimensional interaction with power-law coupling
        cross_dim = np.sum(np.abs(x[:-1] - x[1:])**1.5 * np.sin(0.8 * (x[:-1] + x[1:])))
        
        # Fractional Brownian motion inspired term with long-range dependence
        fbm_term = np.sum(np.sin(2.5 * x) * np.cos(1.8 * x) * 
                         np.sin(1.2 * x) * np.cos(0.9 * x) * 
                         np.exp(-0.1 * np.abs(x)))
        
        # Dimensional complexity adjustment with logarithmic scaling
        dim_adj = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all terms with carefully balanced weights
        return (0.3 * fractal_term + 0.25 * grad_field + 0.2 * harmonic_term + 
                0.1 * cross_dim + 0.1 * fbm_term + 0.05 * geom_factor) * dim_adj