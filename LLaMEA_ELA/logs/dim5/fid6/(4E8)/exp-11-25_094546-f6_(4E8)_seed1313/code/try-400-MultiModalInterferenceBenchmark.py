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
            
            # Base quadratic term with enhanced adaptive curvature
            base = 0.5 * xi**2 * (1.0 + 0.4 * np.sin(self.dim * 0.6 + i * 0.4))
            
            # Enhanced multi-modal sinusoidal components with chaotic frequency modulation
            modal_terms = 0.0
            for k in range(1, 10):
                freq = k * (1.0 + 0.3 * np.sin(i * 0.5 + self.dim * 0.4 + k * 0.2))
                amp = 1.0 / (k**1.7) * (1.0 + 0.15 * np.cos(i * 0.7 + self.dim * 0.3 + k * 0.1))
                modal_terms += amp * np.sin(freq * xi + k * 0.6) * np.cos(freq * xi + k * 0.4)
            
            # Enhanced radial basis function interactions with dynamic sigma
            rbf_interaction = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    sigma = 0.4 + 0.3 * np.sin(i * 0.4 + j * 0.5 + self.dim * 0.2)
                    rbf_interaction += np.exp(-0.5 * (distance/sigma)**2) * np.sin(4 * xi + 3 * x_norm[j] + i * 0.3 + j * 0.2)
            
            # Enhanced adaptive conditioning factor with chaotic modulation
            condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.8 + i * 0.6) * np.cos(xi * 4.0 + self.dim * 0.3)
            
            # Enhanced cross-dimensional coupling with fractal-like scaling
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term += (1.0 / (1.0 + abs(xi - x_norm[j])**4.0)) * np.sin(3 * xi + 4 * x_norm[j] + i * 0.2 + j * 0.3)
            
            # Enhanced multi-scale interference pattern with chaotic phases
            interference = 0.4 * np.sin(9 * xi + 0.6 * i) * np.cos(7 * xi - 0.4 * i) + 0.3 * np.sin(13 * xi + 0.8 * i)
            
            # Enhanced dimensional scaling with chaotic modulation
            dim_scaling = 1.0 + 0.4 * np.sin(self.dim * 0.5 + i * 0.7) * np.cos(self.dim * 0.3 + i * 0.4)
            
            # Add all components together
            result += condition_factor * (base + modal_terms + rbf_interaction + coupling_term + interference) * dim_scaling
            
        # Enhanced global scaling with dimension-dependent correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 2.0) + 0.2 * np.cos(self.dim * 0.4)
        
        return global_scale * result / self.dim