import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher dimensionality influence
        self.chaos_params = np.random.uniform(0.05, 1.2, dim)
        self.energy_well_depths = np.random.uniform(0.5, 6.0, dim)
        # Additional fractal scaling parameters
        self.fractal_scales = np.linspace(0.5, 8.0, min(dim, 8))
    
    def f(self, x):
        # Enhanced normalization with dynamic range adjustment
        x_norm = x / 5.0
        
        # Multi-scale energy wells with compound chaotic modulation
        energy_term = 0.0
        for i in range(self.dim):
            # Compound chaos with sine and cosine combinations
            depth_mod = (1.0 + 0.4 * np.sin(self.chaos_params[i] * x_norm[i]) * 
                        np.cos(2.0 * self.chaos_params[i] * x_norm[i]))
            depth = self.energy_well_depths[i] * depth_mod
            energy_term += depth * np.exp(-0.25 * (x_norm[i] ** 2)) * \
                          (1.0 + 0.3 * np.sin(5 * np.pi * x_norm[i]) * 
                           np.cos(3 * np.pi * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with polynomial interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                # Polynomial coupling strength based on dimension proximity
                coupling_strength = ((i + j) / (self.dim * (self.dim + 1)) * 
                                   (1.0 + 0.5 * np.sin(x_norm[i] * x_norm[j]) * 
                                    np.cos(2 * x_norm[i] * x_norm[j])))
                # Modified interaction with higher-order polynomial terms
                coupling_term += coupling_strength * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(6 * np.pi * (x_norm[i] + x_norm[j])) * \
                               (1.0 + 0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic time-varying landscape with multiple frequency components
        time_freq = 2.0 + 0.5 * np.sin(np.sum(x_norm) * 0.2) * np.cos(np.sum(x_norm) * 0.1)
        time_term = np.sum(np.sin(time_freq * x_norm) * np.cos(time_freq * x_norm) * 
                          np.exp(-0.05 * np.abs(x_norm)) * 
                          (1.0 + 0.1 * np.sin(2 * np.pi * x_norm)))
        
        # Multi-fractal structure with adaptive complexity scaling
        fractal_term = 0.0
        for i, scale in enumerate(self.fractal_scales):
            if i < self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm) * 
                                     np.cos(scale * x_norm) * 
                                     np.exp(-0.1 * scale * np.abs(x_norm)) * 
                                     (1.0 + 0.15 * np.sin(scale * x_norm)))
        
        # Combined fitness with enhanced nonlinearity
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Advanced dynamic bias and noise with memory effects
        dynamic_bias = 0.4 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm) * 
                                              (1.0 + 0.2 * np.sin(np.sum(x_norm))))
        # Adaptive chaotic noise with feedback from previous evaluations
        chaotic_noise = 0.02 * np.random.uniform(-1, 1) * (1.0 + 0.2 * np.sin(np.sum(x_norm)) * 
                                                         np.cos(np.sum(x_norm) * 0.5))
        
        # Add a small perturbation to increase problem sensitivity
        perturbation = 0.005 * np.sum(np.sin(10 * x_norm) * np.cos(10 * x_norm))
        
        return combined + dynamic_bias + chaotic_noise + perturbation