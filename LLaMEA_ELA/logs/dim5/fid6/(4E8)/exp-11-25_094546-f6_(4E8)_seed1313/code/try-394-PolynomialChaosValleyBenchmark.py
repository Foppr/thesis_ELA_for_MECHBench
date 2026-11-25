import numpy as np

class PolynomialChaosValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base polynomial with dynamic exponentiation
            base = xi**4 + 0.5 * xi**3 - 0.3 * xi**2 + 0.1 * xi
            
            # Chaotic polynomial components with multi-scale structure
            chaotic_terms = 0.0
            for k in range(1, 6):
                freq = k * (1.0 + 0.1 * np.sin(i * 0.5 + self.dim * 0.2))
                amp = 0.7 / (k**1.2) * (1.0 + 0.15 * np.cos(i * 0.3 + self.dim * 0.4))
                chaotic_terms += amp * np.sin(freq * xi**2 + k * 0.4) * np.cos(freq * xi**3 + k * 0.2)
            
            # Radial symmetry with multi-dimensional interaction
            radial_interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = np.sqrt((xi - x_norm[j])**2 + 0.1)
                    radial_interaction += (1.0 / (1.0 + distance**3)) * np.sin(4 * xi + 3 * x_norm[j] + i * 0.3 + j * 0.2)
            
            # Dynamic conditioning factor with fractal-like behavior
            condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.6 + i * 0.4) * np.cos(xi * 2.0 + self.dim * 0.3)
            
            # Valley-forming coupling with adaptive depth
            valley_term = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    diff = xi - x_norm[j]
                    depth = 0.5 + 0.3 * np.sin(i * 0.2 + j * 0.3)
                    valley_term += depth * np.exp(-0.5 * (diff/0.3)**2) * np.cos(3 * diff + i * 0.1 + j * 0.2)
            
            # Multi-scale chaotic modulation
            chaos_mod = 0.4 * np.sin(13 * xi + 0.8 * i) * np.cos(9 * xi - 0.6 * i) + 0.3 * np.sin(17 * xi + 0.5 * i)
            
            # Dimensional scaling with adaptive weight
            dim_weight = 1.0 + 0.25 * np.sin(self.dim * 0.5 + i * 0.7) * np.cos(self.dim * 0.3 + i * 0.4)
            
            # Add all components together
            result += condition_factor * (base + chaotic_terms + radial_interaction + valley_term + chaos_mod) * dim_weight
            
        # Global scaling with chaotic modulation
        global_scale = 1.2 + 0.3 * np.sin(np.log(self.dim + 1) * 2.0) * np.cos(self.dim * 0.4)
        
        return global_scale * result / self.dim