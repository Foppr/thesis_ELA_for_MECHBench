import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x**2 * (1.0 + 0.1 * np.sin(3.0 * x)))
        
        # Enhanced chaotic modulation with multi-scale frequency layers
        chaotic_modulation = np.sum(np.sin(2.0 * np.exp(x)) * np.cos(4.0 * x) * 
                                   np.sin(0.5 * np.exp(2.0 * x)) * np.cos(8.0 * x) * 
                                   np.sin(0.1 * np.exp(3.0 * x)))
        
        # Fractal-like ridge structures with recursive scaling and fractional exponents
        ridge_terms = 0.3 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.7)
        
        # High-frequency oscillations with dynamic amplitude modulation and phase shifts
        high_freq = np.sum(np.sin(25.0 * x) * np.cos(12.0 * x) * 
                          (1.0 + 0.4 * np.sin(6.0 * x)) * np.cos(3.0 * x))
        
        # Cross-dimensional exponential interactions with memory effect and time-delayed feedback
        cross_interaction = 0.1 * np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * 
                                         (x[:-1]**4 + x[1:]**4) * 
                                         np.sin(0.5 * x[:-1]))
        
        # Polynomial interaction with fractional powers, mixed signs, and dynamic coefficients
        poly_interaction = 0.07 * np.sum(x**3.7 + 0.4 * x**5.2 - 0.3 * x**2.8)
        
        # Non-smooth composite interactions with step-like discontinuities and random perturbations
        step_interaction = 0.15 * np.sum(np.floor(2.0 * np.sin(x)) * np.cos(x) + 
                                       0.1 * np.random.randn(len(x)))
        
        # Additional chaotic cross-term with time-delayed feedback and dynamic coupling
        chaotic_cross = 0.05 * np.sum(np.sin(5.0 * x[:-1]) * np.cos(4.0 * x[1:]) * 
                                     np.exp(-0.15 * (x[:-1]**2 + x[1:]**2)) * 
                                     np.sin(0.6 * x[:-1]) * np.cos(0.3 * x[1:]))
        
        # Fractional dimensionality scaling with logarithmic modulation and chaotic perturbations
        dim_scaling = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sin(0.2 * self.dim)
        
        return (quadratic + chaotic_modulation + high_freq + cross_interaction + 
                poly_interaction + ridge_terms + step_interaction + chaotic_cross) * dim_scaling