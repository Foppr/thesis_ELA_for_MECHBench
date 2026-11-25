import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x**2 * (1.0 + 0.1 * np.sin(3.0 * x)))
        
        # Enhanced chaotic modulation with modified frequency layers
        chaotic_modulation = np.sum(np.sin(3.0 * np.exp(x)) * np.cos(5.0 * x) * 
                                   np.sin(0.6 * np.exp(2.0 * x)) * np.cos(9.0 * x) * 
                                   np.sin(0.15 * np.exp(3.0 * x)))
        
        # Fractal-like ridge structures with altered scaling and fractional exponents
        ridge_terms = 0.4 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.5)
        
        # High-frequency oscillations with modified amplitude modulation and phase shifts
        high_freq = np.sum(np.sin(30.0 * x) * np.cos(15.0 * x) * 
                          (1.0 + 0.5 * np.sin(7.0 * x)) * np.cos(4.0 * x))
        
        # Cross-dimensional exponential interactions with modified memory effect
        cross_interaction = 0.15 * np.sum(np.exp(-0.25 * np.abs(x[:-1] - x[1:])) * 
                                         (x[:-1]**3.5 + x[1:]**3.5) * 
                                         np.sin(0.6 * x[:-1]))
        
        # Polynomial interaction with different fractional powers and coefficients
        poly_interaction = 0.08 * np.sum(x**4.2 + 0.3 * x**5.8 - 0.2 * x**3.1)
        
        # Non-smooth composite interactions with modified step-like discontinuities
        step_interaction = 0.18 * np.sum(np.floor(2.5 * np.sin(x)) * np.cos(x) + 
                                       0.12 * np.random.randn(len(x)))
        
        # Additional chaotic cross-term with modified coupling and feedback
        chaotic_cross = 0.07 * np.sum(np.sin(6.0 * x[:-1]) * np.cos(5.0 * x[1:]) * 
                                     np.exp(-0.2 * (x[:-1]**2 + x[1:]**2)) * 
                                     np.sin(0.7 * x[:-1]) * np.cos(0.4 * x[1:]))
        
        # Fractional dimensionality scaling with modified logarithmic modulation
        dim_scaling = 1.0 + 0.35 * np.log(self.dim + 1) + 0.06 * np.sin(0.25 * self.dim)
        
        return (quadratic + chaotic_modulation + high_freq + cross_interaction + 
                poly_interaction + ridge_terms + step_interaction + chaotic_cross) * dim_scaling