import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic modulation with multiple frequencies and phase shifts
        chaotic_modulation = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * x**2) * np.sin(3.0 * x**2))
        
        # Adaptive conditioning based on dimension with exponential scaling
        condition_factor = 1.0 + 0.3 * (self.dim - 1) * np.exp(-0.05 * self.dim)
        
        # High-frequency oscillations with varying amplitudes, phase shifts, and dimension-dependent scaling
        high_freq = np.sum(np.sin(20.0 * x + np.pi/6) * np.cos(18.0 * x + np.pi/4) * condition_factor)
        
        # Cross-dimensional interactions with exponential decay, adaptive weights, and multi-modal structure
        cross_interaction = 0.2 * np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2) * np.sin(2.0 * x[:-1]))
        
        # Polynomial interaction with mixed powers, dimension-dependent scaling, and chaotic perturbations
        poly_interaction = 0.08 * np.sum(x**4 + 0.4 * x**6 + np.sin(10.0 * x) * np.cos(8.0 * x))
        
        # Sharp ridges with multi-modal absolute value operations and nonlinear transformations
        ridge_terms = 0.2 * np.sum(np.abs(x[:-2] + x[2:])**1.7 + np.abs(x[:-1] - x[1:])**1.3)
        
        # Saddle-point interactions with sinusoidal modulation, cross-dimensional coupling, and chaotic components
        saddle_interaction = 0.1 * np.sum(np.sin(3.0 * x[:-1]) * np.cos(3.0 * x[1:]) * (x[:-1]**2 + x[1:]**2) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic component with enhanced complexity and multi-modal behavior
        chaotic_component = 0.05 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.sin(2.0 * x**3))
        
        # Multi-modal ridge structure with additional harmonic components
        multimodal_ridge = 0.1 * np.sum(np.sin(4.0 * x)**2 + np.cos(4.0 * x)**2)
        
        return quadratic + chaotic_modulation + high_freq + cross_interaction + poly_interaction + ridge_terms + saddle_interaction + chaotic_component + multimodal_ridge