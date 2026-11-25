import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced spherical component with dynamic scaling
        sphere_term = np.sum(x_norm**2) * (1.0 + 0.2 * np.sin(self.dim * np.pi / 4.0))
        
        # Modified step function with chaotic threshold variation
        step_term = 0.0
        for i in range(self.dim):
            threshold = 0.3 * np.sin(i * np.pi / 2.0 + self.dim * np.pi / 3.0) + 0.1 * np.cos(i * np.pi / 3.0)
            step_term += np.heaviside(x_norm[i] - threshold, 0.5) * (x_norm[i] - threshold)**2.5
        
        # Enhanced logarithmic component with multi-scale chaotic modulation
        log_term = 0.0
        for i in range(self.dim):
            scale = 1.5 + 0.4 * np.sin(i * np.pi / 2.0 + self.dim * np.pi / 4.0)
            mod_freq = 2.0 + 0.5 * np.cos(i * np.pi / 3.0)
            log_term += scale * np.log(1.0 + np.abs(x_norm[i]) * (1.0 + 0.6 * np.sin(mod_freq * x_norm[i])))
        
        # Intensified chaotic modulation with frequency and amplitude coupling
        chaos_term = 0.0
        for i in range(self.dim):
            freq_mod = 4.0 + 3.0 * np.sin(3 * np.pi * x_norm[i] + self.dim * np.pi / 5.0)
            amp_mod = 1.2 + 0.6 * np.cos(4 * np.pi * x_norm[i])
            chaos_term += amp_mod * np.sin(freq_mod * np.pi * x_norm[i]) * np.cos(freq_mod * np.pi * x_norm[i])
        
        # Stronger adaptive conditioning with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 2.0 * (1.0 - np.exp(-0.5 * r)) * np.sin(4 * np.pi * r)**3
        
        # Extended cross-dimensional coupling with non-linear interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.5 + 0.4 * np.sin(3 * np.pi * (i + j) + self.dim * np.pi / 6.0)
                cross_term += coupling_strength * (np.abs(x_norm[i] - x_norm[j])**1.5)
        
        # Enhanced dimensionality-dependent weighting
        dim_weight = 1.2 + 0.4 * self.dim + 0.2 * np.sin(self.dim * np.pi / 3.0) + 0.1 * np.cos(self.dim * np.pi / 5.0)
        
        # Advanced multimodal component with chaotic basin structure
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (1.0 + 0.6 * np.sin(7 * np.pi * x_norm[i] + self.dim * np.pi / 4.0)) * \
                              (1.0 + 0.4 * np.cos(9 * np.pi * x_norm[i])) * \
                              np.exp(-0.3 * (x_norm[i] - 0.3)**2) * \
                              (1.0 + 0.2 * np.sin(5 * np.pi * x_norm[i]))
        
        # Combine all components with increased complexity
        result = dim_weight * (0.3 * sphere_term + 0.25 * step_term + 0.2 * log_term + 
                              0.15 * chaos_term + 0.1 * cross_term + 0.15 * multimodal_term) * cond_factor
        
        return result