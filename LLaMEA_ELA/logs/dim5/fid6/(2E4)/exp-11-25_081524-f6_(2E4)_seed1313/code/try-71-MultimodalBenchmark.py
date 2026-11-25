import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Fractal-like chaotic modulation with nested sinusoidal structures
        chaotic_modulation = np.sum(np.sin(3.0 * np.exp(2.0 * x)) * np.cos(5.0 * np.exp(x)))
        
        # Enhanced ridge structures with fractional exponents and shift parameters
        ridge_terms = 0.2 * np.sum(np.abs(x[:-2] + x[2:] + 0.3)**1.7)
        
        # Cross-dimensional interactions with adaptive coupling strengths
        cross_interaction = 0.08 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2.5 + x[1:]**1.5))
        
        # Hybrid polynomial-exponential interaction with mixed conditioning
        hybrid_interaction = 0.04 * np.sum((x**3) * np.exp(-0.1 * np.abs(x)))
        
        # High-frequency oscillatory term with dynamic amplitude modulation
        high_freq = np.sum(np.sin(20.0 * x) * np.cos(10.0 * x) * (1.0 + 0.5 * np.sin(7.0 * x)))
        
        # Modified polynomial interactions with non-uniform exponents
        poly_interaction = 0.05 * np.sum(x**4 + 0.3 * x**6 + 0.1 * x**8)
        
        # Additional chaotic cross-term with multi-scale coupling
        chaotic_cross = 0.03 * np.sum(np.sin(4.0 * x[:-1]) * np.cos(3.0 * x[1:]) * np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)) * np.sin(2.0 * x[:-1] * x[1:]))
        
        # Fractional conditioning factor to increase problem difficulty
        condition_factor = 1.0 + 0.2 * (self.dim - 1) / self.dim
        
        return quadratic + chaotic_modulation * condition_factor + high_freq + cross_interaction + poly_interaction + ridge_terms + chaotic_cross