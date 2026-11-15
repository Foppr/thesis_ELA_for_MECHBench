import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.tent_map_params = np.random.uniform(0.5, 1.5, dim)
        self.spherical_harmonics = []
        for _ in range(10):
            l = np.random.randint(1, 6)
            m = np.random.randint(-l, l+1)
            self.spherical_harmonics.append((l, m))
        self.adaptive_weights = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        # Tent map chaotic dynamics
        tent = 0.0
        for i in range(self.dim):
            tent += self.tent_map_params[i] * np.abs(x_norm[i] - 0.5) * (1.0 - np.abs(x_norm[i] - 0.5))
        
        # Spherical harmonic interactions
        sph_harm = 0.0
        for l, m in self.spherical_harmonics:
            theta = np.arccos(x_norm[0] if self.dim > 0 else 0.0)
            phi = np.arctan2(x_norm[1] if self.dim > 1 else 0.0, x_norm[0] if self.dim > 0 else 1.0)
            sph_harm += np.real(np.exp(1j * m * phi) * np.sin(l * theta))
        
        # Adaptive gradient modulation
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += self.adaptive_weights[i] * np.sin(x_norm[i] * np.pi) * np.cos(x_norm[i] * np.pi)
        
        # Cross-dimensional coupling with polynomial interaction
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Polynomial and interaction terms
        poly_term = 0.01 * np.sum(x_norm**4)
        interaction_term = 0.05 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Combine all components
        return tent + sph_harm + grad_mod + cross_term + poly_term + interaction_term