import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic modulation with multiple time-varying parameters
        t1 = 0.7 + 0.3 * np.sin(0.5 * self.dim * np.pi / 5.0)
        t2 = 1.2 + 0.8 * np.cos(0.3 * self.dim * np.pi / 7.0)
        freq_mod = 1.0 + 0.4 * np.sin(t1 * x_norm * t2) * np.cos(t2 * x_norm * t1)
        
        # Multi-scale fractal harmonic interference with dynamic phase coupling
        harmonic_sum = np.sum(np.sin(freq_mod * (3 * np.pi * x_norm + 
                                                 0.6 * np.sin(5 * np.pi * x_norm))) * 
                             np.cos(freq_mod * (6 * np.pi * x_norm + 
                                               0.4 * np.cos(7 * np.pi * x_norm))) * 
                             np.sin(freq_mod * (4 * np.pi * x_norm + 
                                               0.5 * np.sin(8 * np.pi * x_norm))))
        
        # Dynamic saddle point landscape with multi-dimensional curvature
        r_squared = np.sum(x_norm**2)
        saddle_term = 1.2 * r_squared * np.exp(-0.15 * r_squared) * \
                     np.prod(np.cos(3 * np.pi * x_norm) + 0.3 * np.sin(6 * np.pi * x_norm))
        
        # Modified coupling with chaotic interaction strengths and cross-dimensional interference
        coupling_strength = np.exp(-0.3 * np.arange(self.dim)) * (1 + 0.2 * np.sin(5 * np.pi * x_norm))
        coupling_term = np.sum(coupling_strength * 
                             np.sin(4 * np.pi * x_norm[:-1]) * 
                             np.cos(4 * np.pi * x_norm[1:]) * 
                             (1 + 0.15 * np.sin(9 * np.pi * x_norm[:-1])) * 
                             np.cos(2 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Enhanced fractal basin with chaotic center and multi-scale perturbations
        center_shift = 0.4 * np.sin(t1 * np.pi * x_norm) * np.cos(t2 * np.pi * x_norm)
        basin = 0.7 * np.exp(-0.6 * np.sum((x_norm - center_shift)**2)) * \
                np.prod(np.sin(6 * np.pi * (x_norm + 0.15)) + 0.25 * np.cos(9 * np.pi * x_norm))
        
        # Adaptive conditioning with enhanced dimensionality scaling and chaotic modulation
        condition_factor = 1.0 + 0.6 * (self.dim - 1) * np.abs(np.sin(t1)) * np.cos(t2)
        
        # Combine all terms with dynamic weighting and additional chaotic interference
        return condition_factor * (harmonic_sum + saddle_term + coupling_term + basin) + \
               0.3 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm))