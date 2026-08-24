import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.well_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.well_depths = np.random.uniform(1.0, 3.0, 10)
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.coupling_strength = np.random.uniform(0.2, 1.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Periodic parabolic wells with adaptive depth
        well_sum = 0.0
        for i in range(10):
            diff = x_norm - self.well_centers[i]
            # Depth varies based on position to create varying difficulty
            adaptive_depth = self.well_depths[i] * (1.0 + 0.2 * np.abs(x_norm).mean())
            well_sum += adaptive_depth * np.sum(diff**2)
        
        # Cross-dimensional coupling with periodic modulation
        coupling = 0.0
        for i in range(self.dim):
            coupling += self.coupling_strength[i] * np.sin(np.pi * (x_norm[i] + x_norm[(i+1) % self.dim])) * \
                       (x_norm[i]**2 + x_norm[(i+1) % self.dim]**2)
        
        # Adaptive noise with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_amplitudes[i] * np.sin(3 * x_norm[i] + 2 * np.cos(7 * x_norm[i])) * \
                    np.cos(2 * x_norm[i] + np.sin(5 * x_norm[i]))
        
        # Polynomial interaction terms for increased complexity
        poly_interaction = 0.05 * np.sum((x_norm[:-1] - x_norm[1:])**4)
        
        # Global minimum at origin with additional sinusoidal modulation
        return well_sum + coupling + noise + poly_interaction + 0.1 * np.sum(np.sin(2 * x_norm)**2)