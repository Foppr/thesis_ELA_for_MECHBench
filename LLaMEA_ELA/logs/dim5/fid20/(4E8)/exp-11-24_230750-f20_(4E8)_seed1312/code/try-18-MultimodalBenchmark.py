import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms
        exp_terms = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2 * np.pi * x))
        
        # Trigonometric patterns with varying frequencies
        trig_pattern = np.sum(np.sin(3.0 * x) * np.cos(7.0 * x))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * (self.dim - 1)
        
        # Quadratic basin with added noise
        quadratic = condition_factor * np.sum(x**2)
        
        # Cross-term interactions with varying weights
        cross_terms = 0.3 * np.sum(x[:-1] * x[1:] * (1 + 0.1 * np.abs(x[:-1] + x[1:])))
        
        # Combined function value
        return quadratic + exp_terms + trig_pattern + cross_terms