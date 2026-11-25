import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base quadratic term with time-variant curvature
            base = 0.5 * xi**2 * (1.0 + 0.3 * np.sin(self.dim * 0.7 + i * 0.5))
            
            # Dynamic phase-shifted sinusoidal components with chaotic modulation
            modal_terms = 0.0
            for k in range(1, 8):
                freq = k * (1.0 + 0.2 * np.sin(i * 0.6 + self.dim * 0.5 + k * 0.3))
                phase = k * 0.4 + 0.3 * np.cos(i * 0.5 + self.dim * 0.4 + k * 0.2)
                amp = 1.0 / (k**1.5) * (1.0 + 0.2 * np.sin(i * 0.3 + k * 0.1))
                modal_terms += amp * np.sin(freq * xi + phase) * np.cos(freq * xi + phase * 0.7)
            
            # Radial basis function interactions with time-varying parameters
            rbf_interaction = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    sigma = 0.3 + 0.2 * np.sin(i * 0.5 + j * 0.6 + self.dim * 0.3)
                    rbf_interaction += np.exp(-0.5 * (distance/sigma)**2) * np.cos(3 * xi + 2 * x_norm[j] + i * 0.2 + j * 0.1)
            
            # Time-variant conditioning factor with chaotic modulation
            condition_factor = 1.0 + 0.4 * np.sin(self.dim * 0.9 + i * 0.7) * np.cos(xi * 3.0 + self.dim * 0.2)
            
            # Cross-dimensional coupling with dynamic weights
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 0.5 + 0.3 * np.sin(i * 0.4 + j * 0.5 + self.dim * 0.3)
                    coupling_term += weight * (xi - x_norm[j])**3.0 * np.sin(2 * xi + 3 * x_norm[j] + i * 0.1 + j * 0.2)
            
            # Chaotic interference pattern with dynamic amplitude
            interference = 0.5 * np.sin(8 * xi + 0.5 * i) * np.cos(6 * xi - 0.3 * i) + 0.4 * np.sin(12 * xi + 0.7 * i)
            
            # Dynamic dimensional scaling with chaotic modulation
            dim_scaling = 1.0 + 0.35 * np.sin(self.dim * 0.6 + i * 0.8) * np.cos(self.dim * 0.4 + i * 0.5)
            
            # Add all components together
            result += condition_factor * (base + modal_terms + rbf_interaction + coupling_term + interference) * dim_scaling
            
        # Global scaling with time-variant correction factor
        global_scale = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 1.5) + 0.15 * np.cos(self.dim * 0.3)
        
        return global_scale * result / self.dim