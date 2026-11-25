import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.95
        self.sin_mod_freq = 2.0
        self.spherical_harmonic_degree = 5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map component with higher chaos
        logistic_term = 0.0
        for i in range(self.dim):
            chaotic_val = 0.5
            for _ in range(15):  # More transient steps
                chaotic_val = self.logistic_r * chaotic_val * (1 - chaotic_val)
            logistic_term += chaotic_val * np.sin(x[i] * 0.7)  # Slight frequency change
            
        # Modified sinusoidal modulation with phase shifts and amplitudes
        sin_mod_term = 0.0
        for i in range(self.dim):
            freq = self.sin_mod_freq + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.2 * np.cos(i * 0.4)
            phase = 0.2 * np.sin(i * 0.5)
            sin_mod_term += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Enhanced spherical harmonics with higher degree interactions
        sph_harm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                sph_harm_term += np.sin((i + 1) * x[i]) * np.cos((j + 1) * x[j]) * np.sin(0.3 * (i + j))
                
        # Cross-dimensional coupling with more complex interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)  # Add small offset to avoid zero
                cross_coupling += np.exp(-dist * 0.5) * (x[i]**3 + x[j]**3)
                
        # Asymmetric conditioning with polynomial scaling
        asym_cond = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(i * 0.7)
            asym_cond += scale_factor * x[i]**5
            
        # Global scaling factor with enhanced nonlinearity
        global_scale = 1.0 + 0.4 * np.tanh(np.sum(x) * 0.5)
        
        # Combine all terms with adjusted weights
        return global_scale * (0.25 * logistic_term + 0.3 * sin_mod_term + 
                              0.2 * sph_harm_term + 0.15 * cross_coupling + 0.1 * asym_cond)