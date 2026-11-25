import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic modulation with multiple frequency components
        chaotic_modulation = np.sum(np.sin(3.0 * np.exp(x)) * np.cos(5.0 * x) * np.sin(2.0 * x**2))
        
        # Multi-scale high-frequency oscillations
        high_freq = np.sum(np.sin(15.0 * x) * np.cos(8.0 * x) * np.exp(-0.1 * x**2))
        
        # Cross-dimensional interactions with exponential decay and adaptive scaling
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        cross_interaction = 0.1 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2)) * condition_factor
        
        # Polynomial interaction with mixed powers and variable coefficients
        poly_interaction = 0.05 * np.sum(x**4 + 0.3 * x**6 + 0.1 * x**8)
        
        # Sharp ridges with asymmetric penalty and multi-dimensional coupling
        ridge_terms = 0.2 * np.sum(np.abs(x[:-2] + x[2:] + 0.3) ** 1.5)
        
        # Additional chaotic cross-term interaction with higher-order coupling
        chaotic_cross = 0.03 * np.sum(np.sin(4.0 * x[:-1]) * np.cos(3.0 * x[1:]) * np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)) * (x[:-1] + x[1:])**2)
        
        # Multi-scale exponential modulation for increased conditioning
        exp_modulation = 0.15 * np.sum(np.exp(-0.05 * np.abs(x)) * np.sin(10.0 * x))
        
        # Mixed-separable and non-separable components with adaptive coupling
        mixed_interaction = 0.08 * np.sum((x[:-1] * x[1:]) ** 2 + (x[:-1] + x[1:]) ** 3)
        
        return quadratic + chaotic_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms + chaotic_cross + exp_modulation + mixed_interaction