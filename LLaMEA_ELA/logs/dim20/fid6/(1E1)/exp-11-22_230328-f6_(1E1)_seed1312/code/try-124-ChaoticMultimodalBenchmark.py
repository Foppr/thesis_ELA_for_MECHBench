import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.2, 0.8, dim)
        self.energy_well_depths = np.random.uniform(1.5, 4.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with chaotic depth modulation
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.4 * np.sin(self.chaos_params[i] * x_norm[i]))
            energy_term += depth * np.exp(-0.25 * (x_norm[i] ** 2)) * (1.0 + 0.3 * np.cos(4 * np.pi * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with modified interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling strength based on dimension indices and input values
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.4 * np.sin(x_norm[i] * x_norm[j]))
                coupling_term += coupling_strength * np.exp(-0.15 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Enhanced time-varying fitness landscape with modified frequency modulation
        time_freq = 1.2 + 0.4 * np.sin(np.sum(x_norm) * 0.2)
        time_term = np.sum(np.sin(time_freq * x_norm) * np.cos(time_freq * x_norm) * 
                          np.exp(-0.05 * np.abs(x_norm)))
        
        # Enhanced multi-scale fractal-like structure with modified complexity
        fractal_term = 0.0
        scales = [1, 2, 3, 4]
        for scale in scales:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm) * 
                                     np.cos(scale * x_norm) * 
                                     np.exp(-0.05 * scale * np.abs(x_norm)))
        
        # Combined fitness with enhanced scaling factor
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Enhanced dynamic bias and chaotic noise with different coefficients
        dynamic_bias = 0.2 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm))
        chaotic_noise = 0.01 * np.random.uniform(-1, 1) * (1.0 + 0.2 * np.sin(np.sum(x_norm)))
        
        return combined + dynamic_bias + chaotic_noise