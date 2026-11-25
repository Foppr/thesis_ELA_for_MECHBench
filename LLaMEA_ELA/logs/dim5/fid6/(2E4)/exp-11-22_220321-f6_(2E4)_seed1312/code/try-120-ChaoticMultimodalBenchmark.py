import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.95
        self.sin_mod_freq = 2.8
        self.spherical_harmonic_degree = 6
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map component with multi-seed initialization
        logistic_term = 0.0
        for i in range(self.dim):
            # Multi-seed chaotic sequence
            seeds = [0.1, 0.3, 0.7, 0.9]
            chaotic_val = 0.0
            for seed in seeds:
                val = seed
                for _ in range(15):  # More transient steps
                    val = self.logistic_r * val * (1 - val)
                chaotic_val += val * np.sin(x[i] + i * 0.1)
            logistic_term += chaotic_val / len(seeds)
            
        # Multi-scale sinusoidal modulation with frequency coupling
        sin_mod_term = 0.0
        for i in range(self.dim):
            freq1 = self.sin_mod_freq + 0.5 * np.sin(i * 0.3)
            freq2 = 0.7 * np.cos(i * 0.4) + 1.2
            phase1 = 0.2 * np.sin(i * 0.5)
            phase2 = 0.15 * np.cos(i * 0.3)
            sin_mod_term += (np.sin(freq1 * x[i] + phase1) * 
                           np.cos(freq2 * x[i] + phase2) * 
                           np.sin(0.3 * i))
            
        # Nested spherical harmonics with higher-order interactions
        sph_harm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    sph_harm_term += (np.sin((i + 1) * x[i]) * 
                                    np.cos((j + 1) * x[j]) * 
                                    np.sin((k + 1) * x[k]) * 
                                    np.cos(0.4 * (i + j + k)))
                    
        # Cross-dimensional coupling with non-linear interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                cross_coupling += np.exp(-dist * 0.5) * (x[i]**3 + x[j]**3)
                
        # Asymmetric conditioning with dynamic scaling factors
        asym_cond = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(i * 0.7) * np.cos(i * 0.4)
            asym_cond += scale_factor * x[i]**5
            
        # Global scaling factor with multi-dimensional influence
        global_scale = 1.0 + 0.5 * np.tanh(np.sum(x)) * np.cos(np.mean(x))
        
        # Combine all terms with adaptive weights
        return global_scale * (0.25 * logistic_term + 0.3 * sin_mod_term + 
                              0.2 * sph_harm_term + 0.15 * cross_coupling + 0.1 * asym_cond)