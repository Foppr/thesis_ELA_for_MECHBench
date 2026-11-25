import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.energy_well_depths = np.random.uniform(3.0, 10.0, dim)
        # Add additional chaotic modulation parameters
        self.modulation_params = np.random.uniform(0.8, 2.5, dim)
        # New spectral modulation parameters
        self.spectral_params = np.random.uniform(1.0, 3.0, dim)
        # Additional noise sensitivity parameters
        self.noise_sensitivity = np.random.uniform(0.02, 0.08, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with multi-scale chaotic depth modulation
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.6 * np.sin(self.chaos_params[i] * x_norm[i] + 
                                                                     0.4 * np.cos(2 * self.modulation_params[i] * x_norm[i])))
            energy_term += depth * np.exp(-0.5 * (x_norm[i] ** 2)) * (1.0 + 0.4 * np.cos(7 * np.pi * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with dynamic interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices, input values and chaos parameters
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.6 * np.sin(x_norm[i] * x_norm[j] + 
                                                                                           0.3 * np.cos(self.chaos_params[i] * self.chaos_params[j])))
                coupling_term += coupling_strength * np.exp(-0.4 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(8 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Enhanced time-varying fitness landscape with multiple frequency modulations
        time_freq1 = 3.0 + 0.5 * np.sin(np.sum(x_norm) * 0.25)
        time_freq2 = 1.5 + 0.3 * np.cos(np.sum(x_norm) * 0.2)
        time_term = np.sum(np.sin(time_freq1 * x_norm) * np.cos(time_freq2 * x_norm) * 
                          np.exp(-0.08 * np.abs(x_norm)))
        
        # Multi-scale fractal-like structure with increased complexity and chaos
        fractal_term = 0.0
        scales = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for scale in scales:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm + 
                                            0.3 * np.cos(scale * x_norm)) * 
                                     np.cos(scale * x_norm + 
                                           0.2 * np.sin(scale * x_norm)) * 
                                     np.exp(-0.15 * scale * np.abs(x_norm)))
        
        # Spectral modulation component for enhanced complexity
        spectral_term = 0.0
        for i in range(self.dim):
            spectral_term += self.spectral_params[i] * np.sin(3 * np.pi * x_norm[i]) * \
                           np.cos(2 * np.pi * x_norm[i]) * \
                           np.exp(-0.2 * (x_norm[i] ** 2))
        
        # Combined fitness with enhanced scaling factor
        combined = energy_term + coupling_term + time_term + fractal_term + spectral_term
        
        # Enhanced dynamic bias and chaotic noise with higher coefficients
        dynamic_bias = 0.7 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm) * 
                                              np.exp(-0.15 * np.abs(x_norm)))
        chaotic_noise = 0.05 * np.random.uniform(-1, 1) * (1.0 + 0.3 * np.sin(np.sum(x_norm) + 
                                                                               0.15 * np.cos(self.dim)))
        
        # Add additional noise sensitivity term
        noise_term = np.sum(self.noise_sensitivity * np.sin(10 * x_norm) * np.exp(-0.05 * (x_norm ** 2)))
        
        return combined + dynamic_bias + chaotic_noise + noise_term