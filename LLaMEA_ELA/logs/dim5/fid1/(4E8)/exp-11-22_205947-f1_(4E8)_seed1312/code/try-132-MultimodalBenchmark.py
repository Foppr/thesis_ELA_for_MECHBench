import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hierarchical Gaussian peaks with varying scales and orientations
        gaussian_term = 0.0
        scales = np.logspace(-2, 1, min(6, self.dim))
        for i in range(self.dim):
            # Multi-scale Gaussian components with dynamic centers
            center = np.sin(0.5 * np.pi * x_norm[i]) * 0.8
            scale = scales[i % len(scales)]
            gaussian_term += np.exp(-0.5 * ((x_norm[i] - center) / scale)**2) * (1 + 0.3 * np.sin(17 * np.pi * x_norm[i]))
        
        # Dynamic conditioning with multi-scale polynomial interactions
        poly_term = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with dynamic exponents based on neighboring dimensions
            exponent = 2 + 0.5 * np.sin(13 * np.pi * x_norm[i])
            neighbor_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    neighbor_sum += np.abs(x_norm[j])
            poly_term += (x_norm[i]**exponent) * (1 + 0.4 * neighbor_sum)
        
        # Cross-scale interference patterns with chaotic modulation
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with frequency modulation based on dimension positions
                freq_i = 5 + (i % 7)
                freq_j = 4 + (j % 6)
                # Dynamic amplitude modulation using sine-cosine combinations
                amp_mod = 1 + 0.3 * np.sin(23 * np.pi * x_norm[i]) * np.cos(19 * np.pi * x_norm[j])
                interference_term += amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j])
        
        # Rotation-equivariant structure with nested symmetry
        rotation_term = 0.0
        for i in range(self.dim):
            # Nested sinusoidal modulation with increasing frequencies
            freq = 2 + 3 * (i % 5)
            rotation_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Multi-scale radial symmetry with dynamic scaling factors
        radial_term = 0.0
        for i in range(self.dim):
            # Radial component with varying influence based on distance from center
            dist = np.abs(x_norm[i])
            scale_factor = 1 + 0.5 * np.sin(29 * np.pi * dist)
            radial_term += scale_factor * (dist**3) * np.cos(7 * np.pi * dist)
        
        # Global modulation with hierarchical structure
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])
        
        # Combine all terms with adaptive weights and noise
        result = 1.2 * gaussian_term + 0.9 * poly_term + 0.8 * interference_term + \
                 0.7 * rotation_term + 0.6 * radial_term + global_mod
        
        # Add chaotic noise to increase algorithmic pressure
        noise = 0.03 * np.sin(53 * np.pi * np.sum(x_norm**2)) * np.cos(41 * np.pi * np.prod(x_norm))
        result += noise
        
        return result