import numpy as np

class NestedParabolicInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Nested parabolic wells with varying depths and radii
        self.well_depths = np.logspace(1.0, 3.5, min(12, dim)) * 0.8
        self.well_radii = np.logspace(0.5, 2.0, min(12, dim)) * 0.6
        # Dynamic conditioning gradients with dimension-specific scaling
        self.conditioning_gradients = np.linspace(0.8, 3.2, min(10, dim)) * 1.1
        # Cross-dimensional interference parameters for complex interaction
        self.interference_params = np.random.uniform(0.5, 2.0, min(8, dim)) * 1.2
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Nested parabolic wells with varying depths and radii
        well_term = 0.0
        for i in range(min(len(self.well_depths), self.dim)):
            depth = self.well_depths[i]
            radius = self.well_radii[i]
            # Nested parabolic shape with higher-order terms for complex curvature
            well_val = depth * (x_norm[i] ** 2) + 0.3 * (x_norm[i] ** 4) + 0.1 * (x_norm[i] ** 6)
            well_term += well_val
            
        # Dynamic conditioning gradients with varying stiffness across dimensions
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_gradients), self.dim)):
            gradient = self.conditioning_gradients[i]
            # Enhanced conditioning with exponential scaling and cubic modulation
            cond_val = gradient * np.exp(0.5 * x_norm[i] ** 2) + 0.4 * (x_norm[i] ** 3)
            conditioning_term += cond_val
            
        # Cross-dimensional interference patterns with phase shifts and coupling
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Interference with dynamic coupling strength and phase modulation
                coupling_strength = self.interference_params[i % len(self.interference_params)]
                phase_shift = np.pi * (i + j) / (self.dim + 1)
                interference_val = coupling_strength * x_norm[i] * x_norm[j] * np.sin(phase_shift + 2.0 * x_norm[i])
                interference_term += interference_val
                
        # Additional multi-scale clustering with varying separation distances
        cluster_term = 0.0
        for i in range(self.dim):
            # Cluster positioning with dynamic spacing and sinusoidal modulation
            cluster_pos = 2.5 * np.sin(0.5 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            # Multi-scale clustering with increasing polynomial orders
            cluster_val = 1.2 * (distance ** 3) + 0.6 * (distance ** 5) + 0.2 * (distance ** 7) + 0.05 * (distance ** 9)
            cluster_term += cluster_val
            
        # Combined terms with adjusted weights for complex landscape characteristics
        result = 1.1 * well_term + 0.85 * conditioning_term + 0.7 * interference_term + 0.6 * cluster_term
        
        # Add adaptive noise with dimensionality-dependent amplitude
        noise_amplitude = 0.03 * (1.0 + 0.07 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise