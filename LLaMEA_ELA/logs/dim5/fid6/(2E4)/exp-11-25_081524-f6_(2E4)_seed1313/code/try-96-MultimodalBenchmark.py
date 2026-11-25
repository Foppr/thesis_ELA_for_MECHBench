import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning and adaptive scaling
        quadratic = np.sum(x**2 * (1.0 + 0.2 * np.sin(2.0 * x) * np.cos(0.5 * x)))
        
        # Nested chaotic modulation with multiple frequency layers and feedback loops
        chaotic_modulation = np.sum(np.sin(4.0 * np.exp(x)) * np.cos(7.0 * x) * 
                                   np.sin(0.8 * np.exp(3.0 * x)) * np.cos(11.0 * x) * 
                                   np.sin(0.2 * np.exp(5.0 * x)) * np.cos(15.0 * x))
        
        # Fractal-like ridge structures with variable fractional exponents and adaptive scaling
        ridge_terms = 0.5 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.7)
        
        # Ultra-high-frequency oscillations with amplitude modulation, phase shifts, and noise injection
        high_freq = np.sum(np.sin(50.0 * x) * np.cos(25.0 * x) * 
                          (1.0 + 0.6 * np.sin(9.0 * x)) * np.cos(5.0 * x) * 
                          np.random.randn(len(x)))
        
        # Dynamic cross-dimensional exponential interactions with time-delayed feedback and memory effects
        cross_interaction = 0.2 * np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * 
                                        (x[:-1]**4.0 + x[1:]**4.0) * 
                                        np.sin(0.8 * x[:-1]) * np.cos(0.3 * x[1:]))
        
        # Polynomial interaction with mixed fractional powers, adaptive coefficients, and dynamic exponents
        poly_interaction = 0.1 * np.sum(x**5.0 + 0.4 * x**6.5 - 0.3 * x**3.7)
        
        # Non-smooth composite interactions with discontinuous step functions and dynamic thresholds
        step_interaction = 0.25 * np.sum(np.floor(3.0 * np.sin(x)) * np.cos(x) + 
                                       0.15 * np.random.randn(len(x)))
        
        # Additional chaotic cross-term with multi-scale coupling, feedback, and variable phase shifts
        chaotic_cross = 0.1 * np.sum(np.sin(7.0 * x[:-1]) * np.cos(6.0 * x[1:]) * 
                                    np.exp(-0.3 * (x[:-1]**2 + x[1:]**2)) * 
                                    np.sin(0.8 * x[:-1]) * np.cos(0.5 * x[1:]))
        
        # Multi-scale dimensionality scaling with fractal-like logarithmic modulation and dynamic adjustments
        dim_scaling = 1.0 + 0.4 * np.log(self.dim + 1) + 0.1 * np.sin(0.3 * self.dim) + 0.05 * np.cos(0.1 * self.dim)
        
        return (quadratic + chaotic_modulation + high_freq + cross_interaction + 
                poly_interaction + ridge_terms + step_interaction + chaotic_cross) * dim_scaling