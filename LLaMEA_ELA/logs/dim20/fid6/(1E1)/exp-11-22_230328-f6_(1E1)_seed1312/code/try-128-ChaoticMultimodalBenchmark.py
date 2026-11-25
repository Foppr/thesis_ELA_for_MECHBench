import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.1, 0.9, dim)
        self.energy_well_depths = np.random.uniform(1.0, 5.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential energy wells with chaotic depth modulation
        energy_term = 0.0
        for i in range(self.dim):
            depth = self.energy_well_depths[i] * (1.0 + 0.3 * np.sin(self.chaos_params[i] * x_norm[i]))
            energy_term += depth * np.exp(-0.3 * (x_norm[i] ** 2)) * (1.0 + 0.2 * np.cos(3 * np.pi * x_norm[i]))
        
        # Cross-dimensional coupling with modified interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified coupling strength based on dimension indices and input values
                coupling_strength = (i + j) / (self.dim * (self.dim + 1)) * (1.0 + 0.3 * np.sin(x_norm[i] * x_norm[j]))
                coupling_term += coupling_strength * np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * \
                               np.sin(4 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Time-varying fitness landscape with modified frequency modulation
        time_freq = 1.5 + 0.3 * np.sin(np.sum(x_norm) * 0.15)
        time_term = np.sum(np.sin(time_freq * x_norm) * np.cos(time_freq * x_norm) * 
                          np.exp(-0.03 * np.abs(x_norm)))
        
        # Multi-scale fractal-like structure with modified complexity
        fractal_term = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm) * 
                                     np.cos(scale * x_norm) * 
                                     np.exp(-0.07 * scale * np.abs(x_norm)))
        
        # Combined fitness with modified scaling factor
        combined = energy_term + coupling_term + time_term + fractal_term
        
        # Add dynamic bias and chaotic noise with different coefficients
        dynamic_bias = 0.3 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm))
        chaotic_noise = 0.015 * np.random.uniform(-1, 1) * (1.0 + 0.15 * np.sin(np.sum(x_norm)))
        
        # Add modified nonlinear interaction terms for enhanced complexity
        nonlinear_interaction = 0.05 * np.sum(np.sin(2 * x_norm) * np.cos(2 * x_norm) * 
                                            np.exp(-0.1 * np.abs(x_norm)))
        
        return combined + dynamic_bias + chaotic_noise + nonlinear_interaction