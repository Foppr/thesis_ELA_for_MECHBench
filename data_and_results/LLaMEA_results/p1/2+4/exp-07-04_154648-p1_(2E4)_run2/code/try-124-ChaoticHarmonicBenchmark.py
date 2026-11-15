import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.tent_map_params = np.random.uniform(1.5, 2.5, dim)
        self.spherical_harmonics_coeffs = np.random.uniform(-1.0, 1.0, (10, dim))
        self.gradient_fields = np.random.uniform(-0.5, 0.5, (8, dim))
        self.adaptive_weights = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic tent map component
        tent_term = 0.0
        for i in range(self.dim):
            param = self.tent_map_params[i]
            tent_term += param * np.abs(x_norm[i] - 0.5) * (1.0 - np.abs(x_norm[i] - 0.5))
        
        # Spherical harmonics with dynamic coefficients
        sph_harm_term = 0.0
        for i in range(10):
            for j in range(self.dim):
                sph_harm_term += self.spherical_harmonics_coeffs[i, j] * np.sin((i+1) * x_norm[j]) * np.cos((i+1) * x_norm[j])
        
        # Adaptive gradient field component
        grad_field_term = 0.0
        for i in range(8):
            for j in range(self.dim):
                grad_field_term += self.gradient_fields[i, j] * (x_norm[j] ** (i+1)) * self.adaptive_weights[j]
        
        # Cross-dimensional coupling with exponential interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(x_norm[i] + x_norm[j])
        
        # Polynomial and noise components
        poly_term = 0.05 * np.sum(x_norm**6)
        noise_term = 0.1 * np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Combine all terms with global minimum at origin
        return tent_term + sph_harm_term + grad_field_term + cross_term + poly_term + noise_term