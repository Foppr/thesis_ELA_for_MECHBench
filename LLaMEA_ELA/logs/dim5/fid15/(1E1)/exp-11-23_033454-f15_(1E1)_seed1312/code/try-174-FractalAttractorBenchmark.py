import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute fractal parameters for each dimension
        self.fractal_dims = 1.2 + 0.8 * np.sin(np.arange(dim) * 0.7)
        self.attractor_freqs = 2.0 + 1.5 * np.cos(np.arange(dim) * 0.9)
        self.conditioning_factors = 1.0 + 0.5 * np.sin(np.arange(dim) * 0.6)
        # Adaptive coupling strengths
        self.coupling_strengths = 0.5 + 0.8 * np.random.rand(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin term with adaptive conditioning
        basin_term = np.sum(self.conditioning_factors * np.abs(x)**(1.5 + 0.3 * np.sin(self.fractal_dims)))
        
        # Multimodal fractal potential with periodic attractors
        multimodal_term = 0.0
        for i in range(self.dim):
            # Periodic attractor potential
            attractor_potential = np.sin(self.attractor_freqs[i] * x[i])**2 + \
                                np.cos(self.attractor_freqs[i] * x[i])**2
            
            # Fractal modulation of the potential
            fractal_mod = 1.0 + 0.4 * np.sin(x[i] * 0.5 + i * 0.3)
            
            # Combined periodic and fractal potential
            multimodal_term += attractor_potential * fractal_mod
        
        # Cross-dimensional coupling with fractal scaling
        coupling_term = 0.0
        for i in range(self.dim):
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Fractal coupling with dimension-specific strength
                    coupling_strength = self.coupling_strengths[i] * (1.0 + 0.3 * np.sin(i * 0.4 + j * 0.3))
                    # Adaptive fractal distance function
                    dist = np.abs(x[i] - x[j])**self.fractal_dims[i]
                    coupling += coupling_strength * np.exp(-dist)
            coupling_term += coupling
        
        # Embedded fractal noise term
        noise_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal noise with varying frequencies
            noise = 0.2 * (np.sin(x[i] * 3.0 + i * 0.5) + 
                          np.cos(x[i] * 5.0 + i * 0.7) + 
                          np.sin(x[i] * 7.0 + i * 0.9))
            noise_term += noise
        
        # Adaptive conditioning term
        condition_term = 0.0
        for i in range(self.dim):
            # Dimension-specific conditioning with fractal scaling
            cond_factor = self.conditioning_factors[i] * (1.5 + 0.5 * np.cos(x[i] * 0.3))
            condition_term += cond_factor * x[i]**4
        
        # Final function value with weighted components
        return 0.6 * basin_term + 1.2 * multimodal_term + 0.8 * coupling_term + 0.5 * noise_term + 0.7 * condition_term