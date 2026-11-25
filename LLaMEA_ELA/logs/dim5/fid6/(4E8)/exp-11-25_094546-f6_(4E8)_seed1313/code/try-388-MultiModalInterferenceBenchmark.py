import numpy as np

class MultiModalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base quadratic term with adaptive curvature
            base = 0.5 * xi**2 * (1.0 + 0.3 * np.sin(self.dim * 0.5 + i * 0.3))
            
            # Multi-modal sinusoidal components with varying frequencies
            modal_terms = 0.0
            for k in range(1, 8):
                freq = k * (1.0 + 0.2 * np.sin(i * 0.4 + self.dim * 0.3))
                amp = 0.8 / (k**1.5) * (1.0 + 0.1 * np.cos(i * 0.6 + self.dim * 0.2))
                modal_terms += amp * np.sin(freq * xi + k * 0.5) * np.cos(freq * xi + k * 0.3)
            
            # Radial basis function interactions with neighboring dimensions
            rbf_interaction = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    sigma = 0.5 + 0.2 * np.sin(i * 0.3 + j * 0.4)
                    rbf_interaction += np.exp(-0.5 * (distance/sigma)**2) * np.sin(3 * xi + 2 * x_norm[j] + i * 0.2 + j * 0.1)
            
            # Adaptive conditioning factor based on dimension and position
            condition_factor = 1.0 + 0.4 * np.sin(self.dim * 0.7 + i * 0.5) * np.cos(xi * 3.0)
            
            # Cross-dimensional coupling with fractal-like scaling
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term += (1.0 / (1.0 + abs(xi - x_norm[j])**3.0)) * np.sin(2 * xi + 3 * x_norm[j] + i * 0.1 + j * 0.2)
            
            # Multi-scale interference pattern
            interference = 0.3 * np.sin(7 * xi + 0.5 * i) * np.cos(5 * xi - 0.3 * i) + 0.2 * np.sin(11 * xi + 0.7 * i)
            
            # Dimensional scaling with chaotic modulation
            dim_scaling = 1.0 + 0.3 * np.sin(self.dim * 0.4 + i * 0.6) * np.cos(self.dim * 0.2 + i * 0.3)
            
            # Add all components together
            result += condition_factor * (base + modal_terms + rbf_interaction + coupling_term + interference) * dim_scaling
            
        # Global scaling with dimension-dependent correction
        global_scale = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 1.5) + 0.1 * np.cos(self.dim * 0.3)
        
        return global_scale * result / self.dim