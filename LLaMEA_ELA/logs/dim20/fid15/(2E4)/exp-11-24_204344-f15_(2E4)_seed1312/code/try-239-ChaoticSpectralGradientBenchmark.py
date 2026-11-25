import numpy as np

class ChaoticSpectralGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.tent_map_a = 1.8
        self.spectral_band_width = 0.3
        self.adaptive_factor = 2.0
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic tent map component for global complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            # Tent map with parameter modulation
            tent_input = (x[i] * self.tent_map_a) % 1.0
            if tent_input < 0.5:
                chaotic_value = 2.0 * tent_input
            else:
                chaotic_value = 2.0 * (1.0 - tent_input)
            chaotic_term += chaotic_value ** 2
        
        # Spectral band interactions with frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            # Multiple frequency bands with dynamic modulation
            freq_band_1 = 3.0 + 2.0 * np.sin(i * 0.5)
            freq_band_2 = 5.0 + 3.0 * np.cos(i * 0.7)
            spectral_term += (np.sin(freq_band_1 * x[i]) * np.cos(freq_band_2 * x[i]) +
                             np.cos(freq_band_1 * x[i]) * np.sin(freq_band_2 * x[i]))
        
        # Adaptive gradient modulation with dimension-dependent scaling
        gradient_term = 0.0
        for i in range(self.dim):
            # Dynamic gradient strength based on position and dimension
            grad_strength = self.adaptive_factor * (1.0 + 0.5 * np.sin(x[i] * 2.0))
            # Modified gradient field with cross-dimension coupling
            local_grad = grad_strength * (x[i] - np.mean(x)) ** 2
            gradient_term += local_grad
        
        # Cross-dimensional coupling with spectral interference
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited but strategic coupling
                # Spectral interference pattern between dimensions
                coupling_freq = 2.0 * (i + j) * np.pi / (self.dim + 1)
                coupling = np.sin(coupling_freq * x[i]) * np.cos(coupling_freq * x[j])
                coupling_term += coupling
        
        # Multi-scale oscillatory basin with varying curvature
        basin_term = 0.0
        for i in range(self.dim):
            # Multiple oscillation scales with different amplitudes
            scale_1 = 2.0 * np.sin(x[i] * 3.0)
            scale_2 = 1.5 * np.cos(x[i] * 7.0)
            basin_term += (scale_1 + scale_2) ** 2
        
        # Asymmetric energy wells with chaotic perturbations
        well_term = 0.0
        for i in range(self.dim):
            # Asymmetric well with chaotic modulation
            well = (x[i] - 1.5)**2 * (x[i] + 1.5)**2
            # Chaotic perturbation layer
            chaotic_perturb = 0.3 * np.sin(x[i] * 25.0) * np.cos(x[i] * 18.0)
            well_term += well + chaotic_perturb
        
        # Final combination with weighted components
        total = (0.3 * chaotic_term + 
                0.25 * spectral_term + 
                0.2 * gradient_term + 
                0.15 * coupling_term + 
                0.05 * basin_term + 
                0.05 * well_term)
        
        # Adaptive scaling based on dimensionality
        scaling = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return total * scaling