import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.chaos_params = np.random.uniform(0.5, 1.5, dim)
        self.energy_well_depths = np.random.uniform(2.0, 8.0, dim)
        self.frequency_modulators = np.random.uniform(0.8, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with chaotic depth modulation and frequency scaling
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.5 * np.sin(self.chaos_params[i] * x_norm[i]))
            freq_scale = self.frequency_modulators[i]
            energy_term += depth * np.exp(-freq_scale * (x_norm[i] ** 2)) * (1.0 + 0.3 * np.cos(freq_scale * 3 * np.pi * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with dynamic interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices and input values
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.5 * np.sin(x_norm[i] * x_norm[j]))
                distance = (x_norm[i] - x_norm[j])**2
                coupling_term += coupling_strength * np.exp(-0.3 * distance) * \
                               np.sin(5 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Time-varying fitness landscape with enhanced frequency modulation and chaos
        time_freq = 2.0 + 0.5 * np.sin(np.sum(x_norm) * 0.2)
        time_term = np.sum(np.sin(time_freq * x_norm) * np.cos(time_freq * x_norm) * 
                          np.exp(-0.05 * np.abs(x_norm)))
        
        # Multi-scale fractal-like structure with increased complexity and chaos
        fractal_term = 0.0
        scales = [1, 2, 3, 4, 5, 6, 7]
        for scale in scales:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm) * 
                                     np.cos(scale * x_norm) * 
                                     np.exp(-0.1 * scale * np.abs(x_norm)) * 
                                     (1.0 + 0.2 * np.sin(scale * np.sum(x_norm))))
        
        # Combined fitness with enhanced scaling and chaotic bias
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Add dynamic bias and stochastic noise with higher variance
        dynamic_bias = 0.5 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm))
        chaotic_noise = 0.03 * np.random.uniform(-1, 1) * (1.0 + 0.3 * np.sin(np.sum(x_norm)))
        
        # Add a highly chaotic perturbation term
        chaos_perturbation = 0.02 * np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        return combined + dynamic_bias + chaotic_noise + chaos_perturbation