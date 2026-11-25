import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Chaotic modulation with sinusoidal oscillations
        chaotic_modulation = np.sum(np.sin(2.0 * np.exp(x)) * np.cos(4.0 * x))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.15 * (self.dim - 1)
        
        # High-frequency oscillations with varying amplitudes
        high_freq = np.sum(np.sin(12.0 * x) * np.cos(6.0 * x)) * condition_factor
        
        # Cross-dimensional interactions with exponential decay
        cross_interaction = 0.05 * np.sum(np.exp(-0.15 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Polynomial interaction with mixed powers
        poly_interaction = 0.03 * np.sum(x**3 + 0.4 * x**5)
        
        # Sharp ridges created by absolute value operations with additional shift
        ridge_terms = 0.15 * np.sum(np.abs(x[:-2] + x[2:] + 0.5))
        
        # Additional chaotic cross-term interaction
        chaotic_cross = 0.02 * np.sum(np.sin(3.0 * x[:-1]) * np.cos(2.0 * x[1:]) * np.exp(-0.05 * (x[:-1]**2 + x[1:]**2)))
        
        return quadratic + chaotic_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms + chaotic_cross