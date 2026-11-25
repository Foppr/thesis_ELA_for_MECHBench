import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Chaotic modulation with sine and cosine combinations
        chaotic_modulation = np.sum(np.sin(np.exp(x)) * np.cos(np.exp(0.5 * x)))
        
        # Multi-scale exponential interactions with higher frequencies
        scale1 = np.sum(np.exp(-0.5 * x**2) * np.sin(8.0 * x))
        scale2 = np.sum(np.exp(-0.2 * x**2) * np.cos(10.0 * x))
        scale3 = np.sum(np.exp(-0.1 * x**2) * np.sin(15.0 * x))
        
        # Adaptive conditioning based on dimension with stronger effect
        condition_factor = 1.0 + 0.5 * (self.dim - 1)
        
        # High-frequency oscillations with varying amplitudes and phases, increased complexity
        high_freq = np.sum(np.sin(20.0 * x) * np.cos(12.0 * x)) * condition_factor
        
        # Cross-dimensional interactions with chaotic decay and stronger coupling
        cross_interaction = 0.2 * np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * (x[:-1]**3 + x[1:]**3))
        
        # Polynomial interaction with mixed powers and chaotic coefficients, increased complexity
        poly_interaction = 0.05 * np.sum(x**4 + 0.5 * x**6 + np.sin(x) * np.cos(2 * x))
        
        # Enhanced sharp ridges with multi-dimensional coupling and non-integer exponents
        ridge_terms = 0.2 * np.sum(np.abs(x[:-2] + x[2:]) ** 1.7)
        
        # Additional chaotic cross-terms with higher dimensional coupling
        chaotic_cross = 0.08 * np.sum(np.sin(x[:-1]) * np.cos(x[1:]) * np.exp(-0.15 * np.abs(x[:-1] - x[1:])))
        
        # Additional high-frequency oscillation component for increased complexity
        extra_oscillation = 0.1 * np.sum(np.sin(25.0 * x) + np.cos(18.0 * x))
        
        # Asymmetric conditioning to increase difficulty
        asymmetry = 0.05 * np.sum(np.abs(x)**3.5)
        
        return quadratic + chaotic_modulation + scale1 + scale2 + scale3 + high_freq + cross_interaction + poly_interaction + ridge_terms + chaotic_cross + extra_oscillation + asymmetry