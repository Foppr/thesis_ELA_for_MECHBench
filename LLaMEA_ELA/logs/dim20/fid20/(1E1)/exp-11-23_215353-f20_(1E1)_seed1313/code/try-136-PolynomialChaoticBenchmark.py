import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with mixed terms
        poly_chaos = np.sum((x**3 + 0.5 * x**2 - 0.3 * x + 1.0) * np.exp(-0.1 * x**2))
        
        # Trigonometric wave interference with adaptive frequencies
        wave_interference = 0.0
        for i in range(self.dim):
            wave_interference += np.sin((i + 1) * x[i] + np.cos((i + 1) * x[i])) * np.cos((i + 1) * x[i] * np.sin(x[i]))
        
        # Adaptive noise component that scales with dimensionality
        noise = np.sum(np.random.normal(0, 0.1 * self.dim, self.dim) * (x**2 + 1))
        
        # Multi-scale radial basis functions with varying bandwidths
        rbf_multi = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = -5.0 + j * 2.5
                sigma = 0.5 + 0.2 * np.sin(i)
                rbf_multi += np.exp(-0.5 * (x[i] - center)**2 / sigma**2)
        
        # Coupled sine-cosine interaction terms
        coupled_terms = np.sum(np.sin(x[:-1]) * np.cos(x[1:]) + np.cos(x[:-1]) * np.sin(x[1:]))
        
        # Fractional polynomial distortion with varying exponents
        frac_poly = np.sum((x**1.7 + 0.8 * x**1.3 - 0.5 * x**0.9 + 1.2 * x + 0.7)**1.2)
        
        # Exponential modulation with adaptive decay rates
        exp_mod = np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(2.0 * x))
        
        # Cross-dimensional interaction with exponential weighting
        cross_interaction = np.sum(np.exp(-np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Global scaling and combination of all terms
        return 0.25 * poly_chaos + 0.20 * wave_interference + 0.15 * noise + 0.12 * rbf_multi + 0.08 * coupled_terms + 0.07 * frac_poly + 0.06 * exp_mod + 0.07 * cross_interaction + 1.5