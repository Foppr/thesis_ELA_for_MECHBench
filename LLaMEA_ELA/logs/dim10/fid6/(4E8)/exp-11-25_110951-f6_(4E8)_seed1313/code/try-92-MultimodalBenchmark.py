import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Time-varying harmonic interference with dynamic frequency modulation
        t = 0.5 + 0.5 * np.sin(self.dim * np.pi / 10.0)
        freq_mod = 1.0 + 0.3 * np.sin(2 * np.pi * x_norm * t)
        
        # Chaotic harmonic sum with varying phase shifts
        harmonic_sum = np.sum(np.sin(freq_mod * (2 * np.pi * x_norm + 
                                                 0.5 * np.sin(3 * np.pi * x_norm))) * 
                             np.cos(freq_mod * (4 * np.pi * x_norm + 
                                               0.3 * np.cos(5 * np.pi * x_norm))))
        
        # Dynamic saddle point landscape with position-dependent curvature
        r_squared = np.sum(x_norm**2)
        saddle_term = 0.8 * r_squared * np.exp(-0.1 * r_squared) * \
                     np.prod(np.cos(2 * np.pi * x_norm) + 0.2 * np.sin(4 * np.pi * x_norm))
        
        # Multi-scale coupling with exponentially decaying interaction strengths
        coupling_strength = np.exp(-0.2 * np.arange(self.dim))
        coupling_term = np.sum(coupling_strength * 
                             np.sin(3 * np.pi * x_norm[:-1]) * 
                             np.cos(3 * np.pi * x_norm[1:]) * 
                             (1 + 0.1 * np.sin(7 * np.pi * x_norm[:-1])))
        
        # Fractal-like basin with time-varying center and chaotic perturbation
        center_shift = 0.3 * np.sin(t * np.pi * x_norm)
        basin = 0.5 * np.exp(-0.5 * np.sum((x_norm - center_shift)**2)) * \
                np.prod(np.sin(5 * np.pi * (x_norm + 0.1)))
        
        # Adaptive conditioning based on dimensionality and chaotic modulation
        condition_factor = 1.0 + 0.4 * (self.dim - 1) * np.abs(np.sin(t))
        
        # Combine all terms with dynamic weighting
        return condition_factor * (harmonic_sum + saddle_term + coupling_term + basin)