import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Logistic map chaotic component
        chaos = 0.0
        r = 3.95
        for i in range(10):
            chaos += np.sum(np.sin(r * x_norm * (1 - x_norm))**2)
        
        # Fractional polynomial terms for non-smoothness
        frac_poly = np.sum(np.abs(x_norm)**1.7) + 0.5 * np.sum(np.abs(x_norm)**2.3)
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.exp(-np.abs(x_norm[i] - x_norm[i+1])) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        sin_mod = 0.0
        for freq in [2, 5, 8, 12]:
            sin_mod += np.sum(np.sin(freq * x_norm)**3)
        
        # Hyperbolic tangent and polynomial mixing
        tanh_poly = np.sum(np.tanh(x_norm)**4 + 0.3 * x_norm**5)
        
        # Boundary repulsion with logarithmic barrier
        boundary = np.sum(np.log(1 + x_norm**2) + 0.1 * np.exp(-x_norm**2))
        
        # Combined chaotic and rugged landscape
        return 0.5 * chaos + 0.3 * frac_poly + 0.2 * cross_term + 0.4 * sin_mod + 0.15 * tanh_poly + 0.25 * boundary