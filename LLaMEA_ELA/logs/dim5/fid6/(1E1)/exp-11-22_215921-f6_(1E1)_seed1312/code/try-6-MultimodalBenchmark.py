import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Chaotic sinusoidal oscillations with varying frequencies
        chaotic = 1.5 * np.sum(np.sin(7 * np.pi * x_norm * np.exp(-0.5 * x_norm**2)) ** 2)
        
        # Adaptive Gaussian peaks with dynamic centers and widths
        gaussian = 0.8 * np.sum(np.exp(-5 * (x_norm - 0.2 * np.sin(3 * x_norm)) ** 2) + 
                               np.exp(-8 * (x_norm + 0.3 * np.cos(2 * x_norm)) ** 2))
        
        # Cross-term interactions to increase problem difficulty
        cross_term = 0.3 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(4 * np.pi * x_norm[:-1]))
        
        # Combine all terms with different weights
        return quadratic + chaotic + gaussian + cross_term