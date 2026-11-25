import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with modified coefficients
        exp_terms = np.sum(0.7 * np.exp(-0.3 * (x**2)) * np.cos(1.5 * np.pi * x))
        
        # Modified trigonometric patterns with higher frequencies
        trig_pattern = np.sum(0.8 * np.sin(4.0 * x) * np.cos(6.0 * x))
        
        # Adaptive conditioning based on dimensionality with slight modification
        condition_factor = 1.0 + 0.15 * (self.dim - 1)
        
        # Quadratic basin with modified weight
        quadratic = condition_factor * np.sum(x**2)
        
        # Adjusted cross-term interactions with different weighting
        cross_terms = 0.4 * np.sum(x[:-1] * x[1:] * (1 + 0.15 * np.abs(x[:-1] + x[1:])))
        
        # Additional nonlinear interaction term
        nonlinear_interaction = 0.2 * np.sum(np.sin(0.5 * x) * np.cos(0.3 * x**2))
        
        # Combined function value
        return quadratic + exp_terms + trig_pattern + cross_terms + nonlinear_interaction