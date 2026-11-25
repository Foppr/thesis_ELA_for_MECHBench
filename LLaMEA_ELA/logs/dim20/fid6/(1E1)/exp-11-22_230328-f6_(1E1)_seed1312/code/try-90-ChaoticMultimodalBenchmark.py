import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential energy wells with chaotic basin structures
        well_term = 0.0
        for i in range(self.dim):
            well_term += np.exp(-0.5 * (x_norm[i] ** 2)) * np.sin(5 * np.pi * x_norm[i]) ** 2
        
        # Cross-dimensional coupling with quadratic interaction terms
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i] ** 2 + x_norm[i+1] ** 2) * np.sin(2 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Time-variant oscillatory component with dynamic frequency modulation
        time_freq = np.sum(np.sin(np.arange(self.dim) * 0.5 + np.pi * np.sum(x_norm)))
        oscillation_term = np.sum(np.cos(time_freq * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale chaotic attractor with fractal-like properties
        chaotic_term = 0.0
        for scale in [1, 2, 3, 4]:
            chaotic_term += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm) * 
                                 np.exp(-0.02 * scale * (x_norm ** 2 + 1)))
        
        # Combined fitness with dynamic global scaling and noise
        combined = well_term + cross_term + oscillation_term + chaotic_term
        
        # Add dimensionality-dependent bias and time-variant noise
        dim_bias = 0.05 * self.dim * np.sum(np.cos(x_norm))
        noise = 0.02 * np.random.rand() * (1 + np.sin(np.sum(x_norm)))
        
        return combined + dim_bias + noise