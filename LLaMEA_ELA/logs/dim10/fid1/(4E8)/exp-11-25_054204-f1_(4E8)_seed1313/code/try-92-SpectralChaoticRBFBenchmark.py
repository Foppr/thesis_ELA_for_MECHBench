import numpy as np

class SpectralChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        # Spectral components for frequency modulation
        self.spectral_coeffs = np.random.randn(5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component with time-varying parameter
        chaotic_term = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                chaotic_term += x[i] * r * (1 - x[i])
            else:
                chaotic_term += x[i-1] * r * (1 - x[i-1]) * np.sin(x[i] * (i+1))
        
        # Radial basis function interpolation component
        rbf_term = 0.0
        for i in range(10):
            diff = x - self.rbf_centers[i]
            rbf_term += self.rbf_widths[i] * np.exp(-0.5 * np.sum(diff**2))
        
        # Spectral decomposition with frequency modulation
        spectral_term = 0.0
        for i in range(5):
            freq_mod = np.sin(x * (i+1) * 0.5)
            spectral_term += self.spectral_coeffs[i] @ np.sin(freq_mod)
        
        # Cross-dimensional coupling with cosine interactions
        coupling_term = 0.0
        for i in range(self.dim-1):
            coupling_term += np.cos(x[i] - x[i+1]) * (i+1) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Polynomial interaction with mixed degrees
        poly_term = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                poly_term += x[i]**6 * np.cos(x[i])
            elif i % 4 == 1:
                poly_term += x[i]**5 * np.sin(x[i])
            elif i % 4 == 2:
                poly_term += x[i]**4 * np.tan(x[i])
            else:
                poly_term += x[i]**3 * np.exp(-x[i]**2)
        
        # Global minimum at origin with additional penalty for distance from center
        penalty = np.sum(x**2) * 0.1
        
        return 1.5 * chaotic_term + 0.8 * rbf_term + 1.2 * spectral_term + 0.7 * coupling_term + 0.6 * poly_term + penalty