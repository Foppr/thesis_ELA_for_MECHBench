import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with sinusoidal conditioning
        quadratic = np.sum(x**2 * (1.0 + 0.2 * np.sin(2.0 * x)))
        
        # Sinusoidal ridge structures with varying frequencies and amplitudes
        ridge_terms = 0.3 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.9 * 
                                  (1.0 + 0.5 * np.sin(4.0 * x[:-1])))
        
        # Asymmetric exponential interactions with skewness control
        skewness_factor = 1.0 + 0.2 * np.tanh(x)
        cross_exp = 0.3 * np.sum(np.exp(-0.4 * np.abs(x[:-1] - x[1:])) * 
                                 (x[:-1]**2.7 * skewness_factor[:-1] + 
                                  x[1:]**2.7 * skewness_factor[1:]))
        
        # Polynomial oscillations with dynamic exponents
        poly_osc = 0.45 * np.sum((x**3.3 + 0.5 * x**4.2) * np.cos(6.0 * x))
        
        # Enhanced chaotic modulation with feedback loops and phase shifts
        chaotic_mod = 0.22 * np.sum(np.sin(7.5 * x + np.sin(3.5 * x)) * 
                                   np.cos(5.5 * x) * np.exp(-0.12 * x**2))
        
        # Skewed polynomial interactions with dimension-dependent scaling
        skewed_poly = 0.25 * np.sum((x**2.9 + 0.3 * x**4.0 - 0.1 * x**2.2) * 
                                   (1.0 + 0.4 * np.sin(0.5 * self.dim + x)))
        
        # Asymmetric ridge coupling with directional preference
        asym_ridge = 0.18 * np.sum(np.abs(x[:-1] - x[1:]) ** 2.5 * 
                                  np.sin(0.55 * x[:-1]) * np.cos(0.55 * x[1:]))
        
        # Final scaling factor with logarithmic dimensionality effect
        dim_factor = 1.0 + 0.35 * np.log(self.dim + 2) + 0.06 * np.sin(0.35 * self.dim)
        
        return (quadratic + ridge_terms + cross_exp + poly_osc + chaotic_mod + 
                skewed_poly + asym_ridge) * dim_factor