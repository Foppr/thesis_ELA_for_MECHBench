import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic modulation with multiple frequencies
        chaotic_modulation = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * x**2))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        
        # High-frequency oscillations with varying amplitudes and phase shifts
        high_freq = np.sum(np.sin(15.0 * x + np.pi/4) * np.cos(12.0 * x + np.pi/3)) * condition_factor
        
        # Cross-dimensional interactions with exponential decay and adaptive weights
        cross_interaction = 0.1 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Polynomial interaction with mixed powers and dimension-dependent scaling
        poly_interaction = 0.05 * np.sum(x**4 + 0.3 * x**6)
        
        # Sharp ridges created by absolute value operations with nonlinear transformations
        ridge_terms = 0.15 * np.sum(np.abs(x[:-2] + x[2:])**1.5)
        
        # Saddle-point interactions with sinusoidal modulation
        saddle_interaction = 0.08 * np.sum(np.sin(2.0 * x[:-1]) * np.cos(2.0 * x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Additional chaotic component for increased complexity
        chaotic_component = 0.03 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)))
        
        return quadratic + chaotic_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms + saddle_interaction + chaotic_component