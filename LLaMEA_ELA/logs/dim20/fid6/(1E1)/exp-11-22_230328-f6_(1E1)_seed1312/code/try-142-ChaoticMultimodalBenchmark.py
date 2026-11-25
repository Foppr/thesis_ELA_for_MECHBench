import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.chaos_params = np.random.uniform(0.5, 1.5, dim)
        self.energy_well_depths = np.random.uniform(2.0, 8.0, dim)
        # Add additional chaotic modulation parameters
        self.modulation_params = np.random.uniform(0.8, 2.0, dim)
        # New hybrid energy well structure parameters
        self.hybrid_params = np.random.uniform(1.0, 3.0, dim)
        # Additional noise sensitivity parameters
        self.noise_sensitivity = np.random.uniform(0.05, 0.2, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with multi-scale chaotic depth modulation and hybrid structures
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.5 * np.sin(self.chaos_params[i] * x_norm[i] + 
                                                                     0.3 * np.cos(2 * self.modulation_params[i] * x_norm[i])))
            # Hybrid energy well structure with additional sinusoidal modulation
            hybrid_mod = 1.0 + 0.2 * np.sin(self.hybrid_params[i] * x_norm[i]**2) * np.cos(self.hybrid_params[i] * x_norm[i])
            energy_term += depth * np.exp(-0.4 * (x_norm[i] ** 2)) * (1.0 + 0.3 * np.cos(5 * np.pi * x_norm[i])) * hybrid_mod
        
        # Enhanced cross-dimensional coupling with dynamic interaction terms and noise sensitivity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices, input values and chaos parameters
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.5 * np.sin(x_norm[i] * x_norm[j] + 
                                                                                           0.2 * np.cos(self.chaos_params[i] * self.chaos_params[j])))
                # Add noise sensitivity factor
                noise_factor = 1.0 + self.noise_sensitivity[i] * np.sin(x_norm[i]) + self.noise_sensitivity[j] * np.cos(x_norm[j])
                coupling_term += coupling_strength * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(6 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(3 * np.pi * (x_norm[i] - x_norm[j])) * noise_factor
        
        # Enhanced time-varying fitness landscape with multiple frequency modulations and additional chaotic components
        time_freq1 = 2.0 + 0.4 * np.sin(np.sum(x_norm) * 0.2)
        time_freq2 = 1.0 + 0.2 * np.cos(np.sum(x_norm) * 0.15)
        # Add additional chaotic modulation to time components
        time_mod1 = 1.0 + 0.1 * np.sin(3 * np.sum(x_norm))
        time_mod2 = 1.0 + 0.1 * np.cos(4 * np.sum(x_norm))
        time_term = np.sum(np.sin(time_freq1 * x_norm) * np.cos(time_freq2 * x_norm) * 
                          np.exp(-0.05 * np.abs(x_norm)) * time_mod1 * time_mod2)
        
        # Multi-scale fractal-like structure with increased complexity and chaos, plus new hybrid components
        fractal_term = 0.0
        scales = [1, 2, 3, 4, 5, 6, 7]
        for scale in scales:
            if scale <= self.dim:
                # Add hybrid fractal component with additional sinusoidal modulation
                hybrid_fractal = np.sin(scale * x_norm + 
                                       0.2 * np.cos(scale * x_norm)) * 
                                np.cos(scale * x_norm + 
                                       0.1 * np.sin(scale * x_norm)) * 
                                np.exp(-0.1 * scale * np.abs(x_norm))
                # Add additional chaotic modulation to fractal term
                chaotic_mod = 1.0 + 0.05 * np.sin(scale * np.sum(x_norm))
                fractal_term += np.sum(hybrid_fractal * chaotic_mod)
        
        # Combined fitness with enhanced scaling factor and new hybrid components
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Enhanced dynamic bias and chaotic noise with higher coefficients and additional hybrid terms
        dynamic_bias = 0.5 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm) * 
                                              np.exp(-0.1 * np.abs(x_norm)))
        # Add new hybrid bias components
        hybrid_bias = 0.2 * np.sum(np.sin(2 * x_norm) * np.cos(3 * x_norm) * 
                                  np.exp(-0.05 * np.abs(x_norm)))
        
        chaotic_noise = 0.03 * np.random.uniform(-1, 1) * (1.0 + 0.25 * np.sin(np.sum(x_norm) + 
                                                                               0.1 * np.cos(self.dim)))
        # Add additional noise components
        additional_noise = 0.01 * np.random.uniform(-1, 1) * np.sum(np.sin(x_norm) * np.cos(2 * x_norm))
        
        return combined + dynamic_bias + hybrid_bias + chaotic_noise + additional_noise