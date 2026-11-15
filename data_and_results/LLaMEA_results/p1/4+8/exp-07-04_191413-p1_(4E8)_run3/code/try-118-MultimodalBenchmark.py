import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees for conditioning
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Trigonometric terms with multiple frequencies and amplitudes
        trig_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                          np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential decay with sinusoidal modulation
        exp_trig = np.sum(np.exp(-x_norm**2) * (1 + 0.5 * np.sin(4 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with interaction weights
        cross_coupling = 0.3 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(2 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Nested chaotic modulation with varying scales
        chaotic_mod = 0.2 * np.sum(np.sin(10 * np.pi * x_norm**2) * np.cos(15 * np.pi * x_norm**3))
        
        # Adaptive conditioning based on dimensionality
        adaptive_cond = 0.1 * np.sum((1 + 0.1 * self.dim) * x_norm**6)
        
        # Combine all terms with different weights
        return poly_term + 0.5 * trig_term + 0.3 * exp_trig + cross_coupling + chaotic_mod + adaptive_cond