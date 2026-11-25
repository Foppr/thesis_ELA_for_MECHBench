import numpy as np

class ChaoticFractalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for dynamic behavior
        self.chaotic_params = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like terrain with recursive scaling
        fractal_terrain = np.sum(np.power(np.abs(x_norm), 1.7) * 
                                (1 + 0.3 * np.sin(10 * x_norm) * np.cos(7 * x_norm)))
        
        # Dynamic correlation structure with time-varying weights
        dynamic_corr = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.sin(self.chaotic_params[i] * x_norm[i])
            dynamic_corr += weight * np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * \
                           np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Chaotic modulation with logistic map behavior
        chaotic_mod = np.sum(2.0 * np.sin(3 * x_norm) * 
                            np.exp(-0.5 * np.abs(x_norm)) * 
                            (1 + 0.4 * np.sin(15 * x_norm)))
        
        # Multi-scale periodic peaks with varying frequencies
        peak_structure = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(4 * np.pi * x_norm) * 
                               np.exp(-0.1 * x_norm**2))
        
        # Time-varying harmonic components
        time_varying = np.sum(np.sin(self.chaotic_params * x_norm) * 
                             np.cos(2 * self.chaotic_params * x_norm) * 
                             (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Adaptive conditioning with exponential scaling
        adaptive_cond = np.sum(np.exp(0.5 * x_norm**2) * 
                              (1 + 0.3 * np.cos(5 * x_norm)) * 
                              (1 + 0.2 * np.sin(8 * x_norm)))
        
        # Cross-dimensional interaction with power-law decay
        cross_dim_interaction = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**0.7 * 
                                     (1 + 0.3 * np.sin(6 * x_norm[:-1])))
        
        # Combined landscape
        return 1.2 * (fractal_terrain + dynamic_corr + chaotic_mod + 
                     peak_structure + time_varying + adaptive_cond + 
                     cross_dim_interaction)