import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.energy_well_depths = np.random.uniform(2.0, 8.0, dim)
        # Add additional chaotic modulation parameters
        self.modulation_params = np.random.uniform(0.1, 0.8, dim)
        self.coupling_strengths = np.random.uniform(0.5, 2.5, (dim, dim))
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential energy wells with multiple chaotic modulations
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.5 * np.sin(self.chaos_params[i] * x_norm[i]))
            depth *= (1.0 + 0.2 * np.cos(self.modulation_params[i] * x_norm[i]**2))
            energy_term += depth * np.exp(-0.4 * (x_norm[i] ** 2)) * (1.0 + 0.3 * np.sin(5 * np.pi * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with dynamic interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices and input values
                coupling_strength = self.coupling_strengths[i][j] * (1.0 + 0.4 * np.sin(x_norm[i] * x_norm[j]))
                coupling_term += coupling_strength * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(6 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Time-varying fitness landscape with multiple frequency components
        time_freq1 = 2.0 + 0.5 * np.sin(np.sum(x_norm) * 0.2)
        time_freq2 = 1.0 + 0.3 * np.cos(np.sum(x_norm) * 0.15)
        time_term = np.sum(np.sin(time_freq1 * x_norm) * np.cos(time_freq2 * x_norm) * 
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
        
        # Additional chaotic perturbation terms
        chaos_perturbation = 0.0
        for i in range(self.dim):
            chaos_perturbation += 0.1 * np.sin(self.chaos_params[i] * x_norm[i]) * \
                                np.cos(self.modulation_params[i] * x_norm[i]**3)
        
        # Combined fitness with modified scaling factors and chaotic additions
        combined = energy_term + coupling_term + time_term + fractal_term + chaos_perturbation
        
        # Add dynamic bias and stochastic noise with higher variance
        dynamic_bias = 0.5 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm) * 
                                             (1.0 + 0.2 * np.sin(np.sum(x_norm))))
        chaotic_noise = 0.03 * np.random.uniform(-1, 1) * (1.0 + 0.3 * np.sin(np.sum(x_norm)))
        
        return combined + dynamic_bias + chaotic_noise