import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Piecewise polynomial with varying exponents to induce non-smoothness
        f2 = np.sum(np.piecewise(x_norm, [x_norm < 0, x_norm >= 0], 
                                [lambda x: x**5, lambda x: x**3]))
        
        # Fractional Brownian motion-inspired irregularities using sine and cosine combinations
        f3 = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * np.exp(-x_norm**2))
        
        # Adaptive sinusoidal modulation with dynamic frequency based on input magnitude
        freq_mod = 5 + 3 * np.abs(x_norm)
        f4 = np.sum(np.sin(freq_mod * x_norm)**4)
        
        # Multi-scale chaotic component using tent map-like behavior
        f5 = np.sum(np.where(np.abs(x_norm) < 0.5, 2 * np.abs(x_norm), 2 - 2 * np.abs(x_norm))**3)
        
        # Logarithmic barrier near boundaries to increase difficulty
        f6 = np.sum(np.log(1 + np.abs(x_norm)**0.7))
        
        # Exponential decay with sinusoidal perturbation for ruggedness
        f7 = np.sum(np.exp(-x_norm**2) * np.sin(15 * x_norm)**2)
        
        # Hyperbolic tangent with variable scaling for additional complexity
        f8 = np.sum(np.tanh(4 * x_norm)**5)
        
        # Power-law decay with oscillatory behavior
        f9 = np.sum(np.abs(x_norm)**1.3 * np.cos(12 * x_norm))
        
        # Combined chaotic and polynomial term with dynamic interaction
        f10 = np.sum((x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2 + 0.1 * x_norm) * 
                     np.sin(8 * x_norm)**3)
        
        # Final weighted combination with dynamic coefficients
        return (0.3 * f1 + 0.2 * f2 + 0.15 * f3 + 0.12 * f4 + 0.1 * f5 + 
                0.08 * f6 + 0.07 * f7 + 0.06 * f8 + 0.05 * f9 + 0.05 * f10)