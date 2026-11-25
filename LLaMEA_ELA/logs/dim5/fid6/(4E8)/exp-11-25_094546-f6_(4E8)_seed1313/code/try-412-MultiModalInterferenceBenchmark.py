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
            
            # Base quadratic term with enhanced adaptive curvature and fractal scaling
            base = 0.5 * xi**2 * (1.0 + 0.6 * np.sin(self.dim * 0.7 + i * 0.5) * np.cos(xi * 3.0 + self.dim * 0.4))
            
            # Enhanced multi-modal sinusoidal components with chaotic frequency modulation and dynamic amplitude
            modal_terms = 0.0
            for k in range(1, 15):
                freq = k * (1.0 + 0.4 * np.sin(i * 0.6 + self.dim * 0.5 + k * 0.3))
                amp = 1.0 / (k**2.0) * (1.0 + 0.2 * np.cos(i * 0.8 + self.dim * 0.4 + k * 0.2))
                phase = k * 0.7 + 0.3 * np.sin(i * 0.5 + k * 0.4)
                modal_terms += amp * np.sin(freq * xi + phase) * np.cos(freq * xi + phase * 0.8)
            
            # Enhanced radial basis function interactions with dynamic sigma and multi-scale influence
            rbf_interaction = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    sigma = 0.5 + 0.4 * np.sin(i * 0.5 + j * 0.6 + self.dim * 0.3)
                    influence = np.exp(-0.5 * (distance/sigma)**2) * np.sin(5 * xi + 4 * x_norm[j] + i * 0.4 + j * 0.3)
                    rbf_interaction += influence * (1.0 + 0.3 * np.cos(xi * 2.0 + x_norm[j] * 1.5))
            
            # Enhanced adaptive conditioning factor with multi-fractal modulation
            condition_factor = 1.0 + 0.7 * np.sin(self.dim * 0.9 + i * 0.7) * np.cos(xi * 5.0 + self.dim * 0.4) * np.sin(xi * 2.0 + i * 0.3)
            
            # Enhanced cross-dimensional coupling with fractal-like scaling and dynamic weights
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 / (1.0 + abs(xi - x_norm[j])**5.0) * (1.0 + 0.2 * np.sin(i * 0.3 + j * 0.4))
                    coupling_term += weight * np.sin(4 * xi + 5 * x_norm[j] + i * 0.2 + j * 0.3)
            
            # Enhanced multi-scale interference pattern with chaotic phases and fractal modulation
            interference = 0.5 * np.sin(11 * xi + 0.7 * i) * np.cos(9 * xi - 0.5 * i) + 0.4 * np.sin(17 * xi + 0.9 * i) + 0.3 * np.sin(23 * xi + 0.6 * i)
            
            # Enhanced dimensional scaling with multi-fractal modulation and dynamic correction
            dim_scaling = 1.0 + 0.5 * np.sin(self.dim * 0.6 + i * 0.8) * np.cos(self.dim * 0.4 + i * 0.5) * (1.0 + 0.2 * np.sin(xi * 3.0 + i * 0.4))
            
            # Add all components together
            result += condition_factor * (base + modal_terms + rbf_interaction + coupling_term + interference) * dim_scaling
            
        # Enhanced global scaling with dimension-dependent correction and multi-fractal modulation
        global_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 1) * 2.5) + 0.3 * np.cos(self.dim * 0.5) * (1.0 + 0.1 * np.sin(self.dim * 0.3))
        
        return global_scale * result / self.dim