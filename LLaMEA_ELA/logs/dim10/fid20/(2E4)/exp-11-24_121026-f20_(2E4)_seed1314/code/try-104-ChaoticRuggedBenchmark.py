import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Logistic map chaotic component with modified parameter
        chaos = 0.0
        r = 3.85  # Slightly reduced chaos intensity
        for i in range(10):
            chaos += np.sum(np.sin(r * x_norm * (1 - x_norm))**2)
        
        # Fractional polynomial terms with altered exponents for increased non-smoothness
        frac_poly = np.sum(np.abs(x_norm)**1.3) + 0.7 * np.sum(np.abs(x_norm)**2.8)  # Changed exponents
        
        # Cross-dimensional interaction with stronger coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.exp(-0.5 * np.abs(x_norm[i] - x_norm[i+1])) * (x_norm[i]**2 + x_norm[i+1]**2)  # Increased coupling strength
        
        # Multi-scale sinusoidal modulation with shifted frequencies
        sin_mod = 0.0
        for freq in [3, 6, 9, 15]:  # Changed frequencies for more complex modulation
            sin_mod += np.sum(np.sin(freq * x_norm)**4)  # Increased exponent for sharper peaks
        
        # Hyperbolic tangent and polynomial mixing with modified weights
        tanh_poly = np.sum(0.8 * np.tanh(x_norm)**4 + 0.2 * x_norm**6)  # Changed coefficients and exponent
        
        # Boundary repulsion with modified logarithmic barrier
        boundary = np.sum(1.2 * np.log(1 + x_norm**2) + 0.05 * np.exp(-x_norm**2))  # Adjusted weights
        
        # Combined chaotic and rugged landscape
        return 0.4 * chaos + 0.4 * frac_poly + 0.3 * cross_term + 0.5 * sin_mod + 0.2 * tanh_poly + 0.3 * boundary