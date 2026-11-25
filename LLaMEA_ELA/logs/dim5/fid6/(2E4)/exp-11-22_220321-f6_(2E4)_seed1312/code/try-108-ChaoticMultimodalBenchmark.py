import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.95
        self.sin_mod_freq = 1.0
        self.spherical_harmonic_degree = 3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component for chaotic behavior
        logistic_term = 0.0
        for i in range(self.dim):
            # Initialize chaotic sequence
            chaotic_val = 0.5
            for _ in range(10):  # Discard initial transient
                chaotic_val = self.logistic_r * chaotic_val * (1 - chaotic_val)
            logistic_term += chaotic_val * np.sin(x[i])
            
        # Sinusoidal modulation with varying frequencies and phases
        sin_mod_term = 0.0
        for i in range(self.dim):
            freq = self.sin_mod_freq + 0.2 * np.sin(i * 0.5)
            phase = 0.1 * np.cos(i * 0.3)
            sin_mod_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Spherical harmonics component
        sph_harm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Simplified spherical harmonic-like interaction
                sph_harm_term += np.sin((i + 1) * x[i]) * np.cos((j + 1) * x[j])
                
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross_coupling += np.exp(-dist * 0.5) * (x[i]**2 + x[j]**2)
                
        # Asymmetric conditioning with dimension-dependent scaling
        asym_cond = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.7)
            asym_cond += scale_factor * x[i]**4
            
        # Global scaling factor based on sum of variables
        global_scale = 1.0 + 0.2 * np.tanh(np.sum(x))
        
        # Combine all terms with dynamic weights
        return global_scale * (0.25 * logistic_term + 0.3 * sin_mod_term + 
                              0.2 * sph_harm_term + 0.15 * cross_coupling + 0.1 * asym_cond)