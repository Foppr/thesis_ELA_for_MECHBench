import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Logarithmic modulation with chaotic sine components
        log_modulation = np.sum(np.log(1.0 + np.abs(x)) * np.sin(np.exp(x)))
        
        # Saddle-point structure using hyperbolic functions
        saddle = np.sum(np.tanh(x) * np.cos(2.0 * x))
        
        # Multi-scale sinusoidal interactions with varying frequencies
        multi_scale = 0.5 * np.sum(np.sin(1.0 * x) + np.sin(3.0 * x) + np.sin(7.0 * x))
        
        # Exponential decay with cross-dimensional coupling
        cross_decay = 0.3 * np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * (x[:-1]**2 + x[1:]**2))
        
        # Polynomial terms with mixed degrees and negative coefficients
        poly_terms = 0.1 * np.sum(x**4 - 0.8 * x**3 + 0.2 * x**2)
        
        # Sharp transitions via sign and absolute value operations
        transition_terms = 0.2 * np.sum(np.abs(np.sin(0.5 * x)) * np.cos(0.3 * x))
        
        return quadratic + log_modulation + saddle + multi_scale + cross_decay + poly_terms + transition_terms