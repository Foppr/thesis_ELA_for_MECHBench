import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with more varied distribution
        self.chaos_params = np.random.uniform(0.5, 1.5, dim)
        self.energy_well_depths = np.random.uniform(2.0, 6.0, dim)
        # Add frequency modulation parameters
        self.freq_modulation = np.random.uniform(0.8, 1.2, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with chaotic depth modulation and frequency scaling
        energy_term = 0.0
        for i in range(self.dim):
            # Enhanced chaotic modulation with frequency scaling
            depth = self.energy_well_depths[i] * (1.0 + 0.4 * np.sin(self.chaos_params[i] * x_norm[i]))
            freq_scale = self.freq_modulation[i]
            energy_term += depth * np.exp(-0.3 * (x_norm[i] ** 2)) * (1.0 + 0.2 * np.cos(freq_scale * 2 * np.pi * x_norm[i]))
        
        # Modified cross-dimensional coupling with stronger interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling strength with dimension-dependent scaling
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.3 * np.sin(x_norm[i] * x_norm[j]))
                # Modified interaction with more pronounced oscillatory behavior
                coupling_term += coupling_strength * np.exp(-0.15 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(4 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Improved time-varying fitness landscape with adaptive frequency
        time_freq = 1.0 + 0.3 * np.sin(np.sum(x_norm) * 0.15)
        time_term = np.sum(np.sin(time_freq * x_norm) * np.cos(time_freq * x_norm) * 
                          np.exp(-0.015 * np.abs(x_norm)))
        
        # Enhanced fractal-like structure with multiple scales and improved complexity
        fractal_term = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            if scale <= self.dim:
                # Improved fractal term with more varied oscillation patterns
                fractal_term += np.sum(np.sin(scale * x_norm) * 
                                     np.cos(scale * x_norm) * 
                                     np.exp(-0.03 * scale * np.abs(x_norm)) * 
                                     (1.0 + 0.1 * np.sin(scale * x_norm)))
        
        # Combined fitness with improved scaling and structure
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Enhanced dynamic bias and chaotic noise with better balance
        dynamic_bias = 0.3 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm))
        chaotic_noise = 0.015 * np.random.uniform(-1, 1) * (1.0 + 0.15 * np.sin(np.sum(x_norm)))
        
        # Add a global scaling factor to improve conditioning
        global_scale = 1.0 + 0.1 * np.abs(np.sum(x_norm))
        
        return combined * global_scale + dynamic_bias + chaotic_noise