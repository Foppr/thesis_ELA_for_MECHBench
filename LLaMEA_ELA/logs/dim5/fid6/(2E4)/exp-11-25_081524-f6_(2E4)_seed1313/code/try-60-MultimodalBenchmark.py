import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic modulation with multiple sinusoidal components
        chaotic_modulation = np.sum(np.sin(2.0 * np.pi * x) * np.cos(7.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Adaptive conditioning based on dimension with exponential scaling
        condition_factor = 1.0 + 0.2 * (self.dim - 1) * np.exp(-0.05 * self.dim)
        
        # High-frequency oscillations with dynamic amplitudes and phase shifts
        high_freq = np.sum(np.sin(15.0 * x + np.sin(x)) * np.cos(8.0 * x + np.cos(x))) * condition_factor
        
        # Cross-dimensional interactions with stronger coupling and exponential decay
        cross_interaction = 0.1 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**3 + x[1:]**3))
        
        # Polynomial interaction with higher-order terms and mixed powers
        poly_interaction = 0.05 * np.sum(x**4 + 0.3 * x**6 + 0.1 * x**8)
        
        # Sharp ridges created by absolute value operations with varying weights
        ridge_terms = 0.2 * np.sum(np.abs(x[:-3] + x[3:]))
        
        # Additional chaotic cross-terms for increased complexity
        chaos_cross = 0.08 * np.sum(np.sin(x[:-2]) * np.cos(x[2:]) * np.exp(-0.1 * np.abs(x[:-2] - x[2:])))
        
        return quadratic + chaotic_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms + chaos_cross