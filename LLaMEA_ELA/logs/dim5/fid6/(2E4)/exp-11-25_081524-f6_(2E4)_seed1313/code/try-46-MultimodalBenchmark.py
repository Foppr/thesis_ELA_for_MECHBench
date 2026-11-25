import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced exponential modulation with sinusoidal oscillations
        exp_modulation = np.sum(np.exp(0.7 * np.sin(x)) * np.cos(4.0 * x))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        
        # High-frequency oscillations with varying amplitudes
        high_freq = np.sum(np.sin(15.0 * x) * np.cos(7.0 * x)) * condition_factor
        
        # Cross-dimensional interactions with exponential decay and additional coupling
        cross_interaction = 0.1 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2 + x[:-1]*x[1:]))
        
        # Polynomial interaction with mixed powers and higher-order terms
        poly_interaction = 0.03 * np.sum(x**4 + 0.3 * x**6)
        
        # Sharp ridges created by absolute value operations with additional nonlinearity
        ridge_terms = 0.15 * np.sum(np.abs(x[:-2] + x[2:]) ** 1.5)
        
        # Additional chaotic component for increased complexity
        chaotic = 0.05 * np.sum(np.sin(np.exp(x)) * np.cos(2.0 * x**2))
        
        return quadratic + exp_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms + chaotic