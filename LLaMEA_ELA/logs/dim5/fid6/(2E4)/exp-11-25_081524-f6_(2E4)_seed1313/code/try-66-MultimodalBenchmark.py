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
        
        # Multi-scale exponential interactions
        scale1 = np.sum(np.exp(-0.5 * x**2) * np.sin(5.0 * x))
        scale2 = np.sum(np.exp(-0.2 * x**2) * np.cos(7.0 * x))
        scale3 = np.sum(np.exp(-0.1 * x**2) * np.sin(11.0 * x))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        
        # High-frequency oscillations with varying amplitudes and phases
        high_freq = np.sum(np.sin(15.0 * x) * np.cos(8.0 * x)) * condition_factor
        
        # Cross-dimensional interactions with chaotic decay
        cross_interaction = 0.1 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**3 + x[1:]**3))
        
        # Polynomial interaction with mixed powers and chaotic coefficients
        poly_interaction = 0.03 * np.sum(x**4 + 0.3 * x**6 + np.sin(x))
        
        # Enhanced sharp ridges with multi-dimensional coupling
        ridge_terms = 0.15 * np.sum(np.abs(x[:-2] + x[2:]) ** 1.5)
        
        # Additional chaotic cross-terms
        chaotic_cross = 0.05 * np.sum(np.sin(x[:-1]) * np.cos(x[1:]) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # Introduce additional complexity with fractional powers and log-modulation
        fractional_term = 0.1 * np.sum(np.abs(x)**1.7 * np.sin(3.0 * x))
        
        # Add a small noise-like component to increase robustness
        noise_component = 0.02 * np.sum(np.sin(25.0 * x) * np.cos(13.0 * x))
        
        return quadratic + chaotic_modulation + scale1 + scale2 + scale3 + high_freq + cross_interaction + poly_interaction + ridge_terms + chaotic_cross + fractional_term + noise_component