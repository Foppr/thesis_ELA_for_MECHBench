import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with dynamic conditioning
        exp_decay = np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(2.0 * x))
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_osc = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) + 
                        np.sin(3.0 * x) * np.cos(6.0 * x))
        
        # Polynomial interaction terms with mixed exponents
        poly_interaction = 0.1 * np.sum(x[:-1]**2 * x[1:]**4 + x[:-1]**4 * x[1:]**2)
        
        # Dynamic conditioning with adaptive scaling factors
        condition_factors = np.array([1.0 + 0.5 * np.sin(0.5 * i) for i in range(self.dim)])
        conditioned_terms = np.sum(condition_factors * x**3)
        
        # Global scaling and normalization
        global_scale = 1.0 / (1.0 + np.exp(-0.1 * np.sum(x**2)))
        
        # Chaotic modulation with nested sinusoidal components
        chaotic_mod = 0.15 * np.sum(np.sin(x**2) * np.cos(x**3) + 
                                  np.sin(x**4) * np.cos(x**5))
        
        # Combined function value with global scaling
        return global_scale * (exp_decay + sin_osc + poly_interaction + 
                              conditioned_terms + chaotic_mod)