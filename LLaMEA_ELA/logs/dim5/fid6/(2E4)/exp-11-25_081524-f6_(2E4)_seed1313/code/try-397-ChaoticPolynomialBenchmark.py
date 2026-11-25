import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Hyperbolic tangent modulated polynomial terms
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**7 - 4*xi**5 + 6*xi**3 - 4*xi
            tan_mod = np.tanh(xi / 2.0)
            result += tan_mod * poly_term * np.exp(-abs(xi)/3.0)
        
        # Polynomial chaos interactions with fractional scaling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                frac_power = 0.5 + 0.3 * np.sin(xi + xj)
                interaction = (xi**frac_power) * (xj**(2.0 - frac_power))
                result += interaction * np.exp(-abs(xi-xj)/4.0)
        
        # Fractional Brownian motion inspired correlations
        for i in range(self.dim):
            xi = x[i]
            fbm_term = np.sin(xi**3) * np.cos(xi**2)
            result += 0.8 * fbm_term * np.exp(-abs(xi)/5.0)
        
        # Multi-scale chaotic sinusoidal components
        for i in range(1, 6):
            freq = i * (1.0 + 0.4 * np.sin(xi / 3.0) if i < self.dim else 1.0)
            chaos_factor = 1.0 + 0.5 * np.tanh(xi * x[i % self.dim] if i < self.dim else xi)
            result += chaos_factor * np.sin(freq * xi) * np.cos(freq * xi) * np.exp(-abs(xi)/2.0)
        
        # Discontinuous piecewise polynomial terms
        for i in range(self.dim):
            xi = x[i]
            if xi < 0:
                result += 0.3 * (xi**4 - 2*xi**2) * np.exp(-abs(xi)/4.0)
            else:
                result += 0.5 * (xi**3 - xi**2) * np.exp(-abs(xi)/3.0)
        
        # Cross-dimensional chaotic coupling with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                weight = 0.7 + 0.3 * np.tanh(xi * xj)
                coupling = np.sin(xi * xj) * np.cos(xi + xj)
                result += weight * coupling * np.exp(-abs(xi-xj)/6.0)
        
        # Adaptive chaotic modulation with exponential decay
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            chaos_mod = 1.0 + 0.4 * np.sin(r) * np.cos(r / 2.0)
            result += chaos_mod * np.exp(-r/4.0)
        
        # High-frequency chaotic noise components
        for i in range(self.dim):
            xi = x[i]
            noise = np.sin(20 * xi) * np.cos(15 * xi)
            result += 0.2 * noise * np.exp(-abs(xi)/3.0)
        
        # Basin boundary irregularity with discontinuous transitions
        basin_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            if abs(xi) > 4.0:
                basin_penalty += 2.0 * (abs(xi) - 4.0)**2
        result += basin_penalty
        
        return result