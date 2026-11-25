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
        ridge_terms = 0.3 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.7 * 
                                  (1.0 + 0.5 * np.sin(4.0 * x[:-1])))
        
        # Asymmetric exponential interactions with skewness control
        skewness_factor = 1.0 + 0.2 * np.tanh(x)
        cross_exp = 0.25 * np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * 
                                 (x[:-1]**2.5 * skewness_factor[:-1] + 
                                  x[1:]**2.5 * skewness_factor[1:]))
        
        # Polynomial oscillations with dynamic exponents
        poly_osc = 0.4 * np.sum((x**3.2 + 0.5 * x**4.1) * np.cos(6.0 * x))
        
        # Chaotic modulation with feedback loops and phase shifts
        chaotic_mod = 0.18 * np.sum(np.sin(7.0 * x + np.sin(3.0 * x)) * 
                                   np.cos(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Skewed polynomial interactions with dimension-dependent scaling
        skewed_poly = 0.22 * np.sum((x**2.8 + 0.3 * x**3.9 - 0.1 * x**2.1) * 
                                   (1.0 + 0.4 * np.sin(0.5 * self.dim + x)))
        
        # Asymmetric ridge coupling with directional preference
        asym_ridge = 0.15 * np.sum(np.abs(x[:-1] - x[1:]) ** 2.3 * 
                                  np.sin(0.5 * x[:-1]) * np.cos(0.5 * x[1:]))
        
        # Final scaling factor with logarithmic dimensionality effect
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 2) + 0.05 * np.sin(0.3 * self.dim)
        
        return (quadratic + ridge_terms + cross_exp + poly_osc + chaotic_mod + 
                skewed_poly + asym_ridge) * dim_factor