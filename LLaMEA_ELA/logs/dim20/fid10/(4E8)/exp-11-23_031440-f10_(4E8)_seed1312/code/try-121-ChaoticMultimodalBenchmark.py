import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component with adaptive conditioning
        sphere_term = np.sum(x_norm**2)
        
        # Step function component with varying thresholds
        step_term = 0.0
        for i in range(self.dim):
            threshold = 0.5 * np.sin(i * np.pi / 4.0)  # Dynamic thresholds
            step_term += np.heaviside(x_norm[i] - threshold, 0.5) * (x_norm[i] - threshold)**2
        
        # Logarithmic interference with multi-scale modulation
        log_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.cos(i * np.pi / 3.0)  # Adaptive scales
            log_term += scale * np.log(1.0 + np.abs(x_norm[i]) * (1.0 + 0.5 * np.sin(i * np.pi / 2.0)))
        
        # Multi-scale chaotic modulation with dynamic coupling
        chaos_term = 0.0
        for i in range(self.dim):
            freq_mod = 3.0 + 2.0 * np.sin(2 * np.pi * x_norm[i])  # Frequency modulation
            amp_mod = 1.0 + 0.4 * np.cos(3 * np.pi * x_norm[i])    # Amplitude modulation
            chaos_term += amp_mod * np.sin(freq_mod * np.pi * x_norm[i]) * np.cos(freq_mod * np.pi * x_norm[i])
        
        # Adaptive conditioning based on input magnitude and dimensionality
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 1.5 * (1.0 - np.exp(-0.3 * r)) * np.sin(3 * np.pi * r)**2
        
        # Cross-dimensional coupling with varying strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling range
                coupling_strength = 0.4 + 0.3 * np.sin(2 * np.pi * (i + j))  # Adaptive coupling
                cross_term += coupling_strength * np.abs(x_norm[i] - x_norm[j])
        
        # Dimensionality-dependent weighting
        dim_weight = 1.0 + 0.3 * self.dim + 0.15 * np.sin(self.dim * np.pi / 4.0)
        
        # Combine all components with modified blending
        result = dim_weight * (0.3 * sphere_term + 0.25 * step_term + 0.2 * log_term + 
                              0.15 * chaos_term + 0.1 * cross_term) * cond_factor
        
        return result