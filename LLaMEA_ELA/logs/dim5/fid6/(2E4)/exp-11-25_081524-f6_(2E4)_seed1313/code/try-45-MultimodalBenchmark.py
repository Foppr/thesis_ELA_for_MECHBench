import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Exponential modulation with sinusoidal oscillations
        exp_modulation = np.sum(np.exp(0.5 * np.sin(x)) * np.cos(3.0 * x))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.1 * (self.dim - 1)
        
        # High-frequency oscillations with varying amplitudes
        high_freq = np.sum(np.sin(10.0 * x) * np.cos(5.0 * x)) * condition_factor
        
        # Cross-dimensional interactions with exponential decay
        cross_interaction = 0.05 * np.sum(np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Polynomial interaction with mixed powers
        poly_interaction = 0.02 * np.sum(x**3 + 0.5 * x**5)
        
        # Sharp ridges created by absolute value operations
        ridge_terms = 0.1 * np.sum(np.abs(x[:-2] + x[2:]))
        
        return quadratic + exp_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms