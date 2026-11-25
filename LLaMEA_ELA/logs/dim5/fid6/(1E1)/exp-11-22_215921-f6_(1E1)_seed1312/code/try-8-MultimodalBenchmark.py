import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Chaotic sinusoidal oscillations with varying frequencies and amplitudes
        chaotic = 2.0 * np.sum(np.sin(9 * np.pi * x_norm * np.exp(-0.3 * x_norm**2)) ** 2)
        
        # Adaptive Gaussian peaks with dynamic centers, widths, and heights
        gaussian = 1.0 * np.sum(
            1.5 * np.exp(-4 * (x_norm - 0.3 * np.sin(4 * x_norm)) ** 2) +
            0.8 * np.exp(-6 * (x_norm + 0.2 * np.cos(3 * x_norm)) ** 2) +
            1.2 * np.exp(-3 * (x_norm - 0.4 * np.tan(2 * x_norm)) ** 2)
        )
        
        # Enhanced cross-term interactions with non-linear coupling
        cross_term = 0.5 * np.sum(
            x_norm[:-1] * x_norm[1:] * np.sin(6 * np.pi * x_norm[:-1] * x_norm[1:]) +
            (x_norm[:-2] + x_norm[1:-1]) * x_norm[2:] * np.cos(3 * np.pi * (x_norm[:-2] + x_norm[1:-1]))
        )
        
        # Additional harmonic and exponential components for increased complexity
        harmonic = 0.7 * np.sum(np.sin(5 * x_norm) ** 4 + np.cos(4 * x_norm) ** 3)
        
        # Combine all terms with different weights
        return quadratic + chaotic + gaussian + cross_term + harmonic