import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced chaotic component with multiple logistic maps and higher dimensionality
        chaos = 0.0
        r_values = [3.55, 3.75, 3.95]  # Multiple chaotic parameters for increased complexity
        for r in r_values:
            for i in range(15):  # More iterations for stronger chaos
                x_norm = r * x_norm * (1 - x_norm)
                chaos += np.sum(np.sin(x_norm)**2)
        
        # Multi-modal fractional polynomial with higher exponents and additional terms
        frac_poly = 0.0
        exponents = [1.1, 1.7, 2.3, 3.1]  # Increased non-smoothness through higher exponents
        weights = [0.8, 0.6, 0.4, 0.2]
        for exp, weight in zip(exponents, weights):
            frac_poly += weight * np.sum(np.abs(x_norm)**exp)
        
        # Stronger cross-dimensional coupling with trigonometric interaction
        cross_term = 0.0
        for i in range(self.dim - 2):  # Extended coupling range
            diff = x_norm[i] - x_norm[i+1]
            cross_term += np.exp(-0.3 * np.abs(diff)) * (np.sin(x_norm[i]) + np.cos(x_norm[i+1]))
        
        # Multi-scale sinusoidal modulation with increased frequency components and sharper peaks
        sin_mod = 0.0
        frequencies = [2, 4, 7, 11, 19]  # More diverse frequency spectrum
        for freq in frequencies:
            sin_mod += np.sum(np.sin(freq * x_norm)**6)  # Even higher exponent for sharper peaks
        
        # Hyperbolic tangent and polynomial mixing with more complex interaction
        tanh_poly = np.sum(0.9 * np.tanh(x_norm)**5 + 0.1 * x_norm**7)  # Increased exponents
        
        # Enhanced boundary repulsion with multiple barrier functions
        boundary = np.sum(1.5 * np.log(1 + x_norm**2) + 0.1 * np.exp(-x_norm**2) + 0.05 * x_norm**4)
        
        # Combined landscape with adjusted weights for increased ruggedness
        return 0.6 * chaos + 0.5 * frac_poly + 0.4 * cross_term + 0.7 * sin_mod + 0.3 * tanh_poly + 0.4 * boundary