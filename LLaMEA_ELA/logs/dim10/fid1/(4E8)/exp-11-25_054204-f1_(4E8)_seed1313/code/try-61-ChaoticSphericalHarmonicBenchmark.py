import numpy as np

class ChaoticSphericalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.harmonic_coeffs = np.random.randn(dim, 3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical harmonic component
        spherical_harmonic = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            theta = np.arctan2(x[i], x[(i+1)%self.dim]) if self.dim > 1 else 0
            phi = np.arccos(x[i] / (r + 1e-8))
            spherical_harmonic += self.harmonic_coeffs[i, 0] * np.sin(self.harmonic_coeffs[i, 1] * theta) * np.cos(self.harmonic_coeffs[i, 2] * phi)
        
        # Chaotic logistic map component
        logistic = 0.0
        r_val = 3.95
        for i in range(self.dim):
            x_i = (x[i] + 5.0) / 10.0  # Normalize to [0,1]
            logistic += r_val * x_i * (1 - x_i)
        
        # Adaptive noise component
        noise = np.random.normal(0, 0.1 * (1 + np.abs(np.mean(x))), self.dim)
        adaptive_noise = np.sum(noise**2)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-0.1 * (i-j)**2) * x[i] * x[j]
        
        # Polynomial interaction with mixed degrees
        poly_interaction = 0.5 * np.sum(x**3) + 0.3 * np.sum(x**5)
        
        # Basin attraction term with multiple local minima
        basin_term = 0.0
        for i in range(5):
            center = np.random.uniform(-4, 4, self.dim)
            basin_term += 1.0 / (1.0 + np.sum((x - center)**2))
        
        # Combine all components
        result = spherical_harmonic + logistic + adaptive_noise + cross_coupling + poly_interaction + basin_term
        
        return result