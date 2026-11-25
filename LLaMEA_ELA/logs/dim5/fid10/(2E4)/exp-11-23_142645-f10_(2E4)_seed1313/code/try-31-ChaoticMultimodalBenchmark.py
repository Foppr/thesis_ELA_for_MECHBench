import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with fractal-like sine modulations
        chaos = 0.0
        r = 3.99
        x_shifted = np.roll(x, 1)
        for i in range(7):
            logistic = r * x * (1 - x)
            fractal_mod = np.sin(np.pi * x) * np.cos(2 * np.pi * x)
            chaos += np.sum(logistic + 0.2 * fractal_mod * x_shifted)
            x_shifted = np.roll(x_shifted, 1)
        
        # High-order polynomial terms with varying exponents and coefficients
        poly_terms = np.sum(0.1 * x**3 + 0.05 * x**5 + 0.02 * x**7 + 0.01 * x**9 + 
                           0.005 * x**11)
        
        # Asymmetric sine-wave perturbations with fractal frequency modulation
        asym_sine = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.abs(x)**1.5 + 
                          0.3 * np.sin(6.0 * x) * np.cos(8.0 * x) * np.abs(x)**2.0)
        
        # Cross-term interactions with multi-scale exponential decay and cosine modulation
        cross_terms = np.sum(np.exp(-0.3 * np.abs(x)) * (x**4 + 0.2 * x**6 + 0.05 * x**8) * 
                            np.cos(0.7 * x) * np.sin(0.3 * x))
        
        # Adaptive noise component with phase shifts and amplitude modulation
        noise = np.sum(1.2 * np.sin(1.5 * x + 0.5) + 0.8 * np.cos(2.5 * x - 0.5) + 
                      0.6 * np.sin(3.5 * x + 1.0) + 0.4 * np.cos(4.5 * x - 1.0))
        
        # Global shaping term with multi-scale sinusoidal modulation
        global_term = 0.02 * np.sum(x**2 * np.sin(0.2 * x) * np.cos(0.1 * x))
        
        # Additional fractal-like component with recursive sine-wave interactions
        fractal_component = np.sum(np.sin(np.pi * np.sin(np.pi * x)) * 
                                 np.cos(np.pi * np.cos(np.pi * x)) * 0.5 * np.abs(x))
        
        return poly_terms + asym_sine + cross_terms + noise + 0.03 * chaos + global_term + fractal_component