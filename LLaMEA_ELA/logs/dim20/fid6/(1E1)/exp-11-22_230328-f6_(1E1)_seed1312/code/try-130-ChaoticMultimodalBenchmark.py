import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.chaos_params = np.random.uniform(0.5, 1.5, dim)
        self.energy_well_depths = np.random.uniform(2.0, 8.0, dim)
        # Add additional chaotic modulation parameters
        self.modulation_params = np.random.uniform(0.8, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with multi-scale chaotic depth modulation
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.5 * np.sin(self.chaos_params[i] * x_norm[i] + 
                                                                     0.3 * np.cos(2 * self.modulation_params[i] * x_norm[i])))
            energy_term += depth * np.exp(-0.4 * (x_norm[i] ** 2)) * (1.0 + 0.3 * np.cos(5 * np.pi * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with dynamic interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices, input values and chaos parameters
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.5 * np.sin(x_norm[i] * x_norm[j] + 
                                                                                           0.2 * np.cos(self.chaos_params[i] * self.chaos_params[j])))
                coupling_term += coupling_strength * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(6 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Enhanced time-varying fitness landscape with multiple frequency modulations
        time_freq1 = 2.0 + 0.4 * np.sin(np.sum(x_norm) * 0.2)
        time_freq2 = 1.0 + 0.2 * np.cos(np.sum(x_norm) * 0.15)
        time_term = np.sum(np.sin(time_freq1 * x_norm) * np.cos(time_freq2 * x_norm) * 
                          np.exp(-0.05 * np.abs(x_norm)))
        
        # Multi-scale fractal-like structure with increased complexity and chaos
        fractal_term = 0.0
        scales = [1, 2, 3, 4, 5, 6, 7]
        for scale in scales:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm + 
                                            0.2 * np.cos(scale * x_norm)) * 
                                     np.cos(scale * x_norm + 
                                           0.1 * np.sin(scale * x_norm)) * 
                                     np.exp(-0.1 * scale * np.abs(x_norm)))
        
        # Combined fitness with enhanced scaling factor
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Enhanced dynamic bias and chaotic noise with higher coefficients
        dynamic_bias = 0.5 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm) * 
                                              np.exp(-0.1 * np.abs(x_norm)))
        chaotic_noise = 0.03 * np.random.uniform(-1, 1) * (1.0 + 0.25 * np.sin(np.sum(x_norm) + 
                                                                               0.1 * np.cos(self.dim)))
        
        return combined + dynamic_bias + chaotic_noise