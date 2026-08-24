import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.tent_maps = np.random.uniform(0.5, 1.5, dim)
        self.spherical_harmonics = []
        self.harmonic_orders = []
        for _ in range(10):
            l = np.random.randint(2, 6)
            m = np.random.randint(-l, l+1)
            self.spherical_harmonics.append((l, m))
            self.harmonic_orders.append(np.random.uniform(0.5, 2.0))
        self.gradient_fields = np.random.uniform(-0.5, 0.5, (5, dim))
        self.adaptive_weights = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        result = 0.0
        
        # Chaotic tent map components
        tent_term = 0.0
        for i in range(self.dim):
            tent_map = self.tent_maps[i]
            xi = x_norm[i]
            if xi < 0.5:
                tent_val = tent_map * xi
            else:
                tent_val = tent_map * (1 - xi)
            tent_term += tent_val * np.sin(2 * np.pi * xi)
        
        # Spherical harmonics
        sph_term = 0.0
        for i, (l, m) in enumerate(self.spherical_harmonics):
            r = np.sqrt(np.sum(x_norm**2))
            theta = np.arccos(x_norm[0] / (r + 1e-8))
            phi = np.arctan2(x_norm[1], x_norm[0])
            sph_val = np.sin(l * theta) * np.cos(m * phi) * self.harmonic_orders[i]
            sph_term += sph_val / (r + 1e-8)
        
        # Adaptive gradient fields
        grad_term = 0.0
        for i in range(5):
            diff = x_norm - self.gradient_fields[i]
            dist = np.sqrt(np.sum(diff**2))
            grad_term += np.exp(-dist**2) * np.sum(diff**2)
        
        # Adaptive weighting and polynomial interaction
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.adaptive_weights[i] * x_norm[i]**4
        
        # Cross-dimension interaction with dynamic coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            coupling = 0.5 + 0.5 * np.sin(np.pi * x_norm[i] * x_norm[i+1])
            cross_term += coupling * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Global minimum at origin with added noise
        result = tent_term + sph_term + grad_term + poly_term + cross_term
        
        # Add noise component
        noise = 0.01 * np.sum(np.sin(10 * x_norm)**2)
        result += noise
        
        return result