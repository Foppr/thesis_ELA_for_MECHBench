import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        freq1 = 3 * np.pi
        freq2 = 7 * np.pi
        sinusoidal_term = np.sum(np.sin(freq1 * x_normalized)**2 + 0.5 * np.sin(freq2 * x_normalized)**2)
        
        # High-frequency oscillations with interaction terms for increased complexity
        high_freq_term = np.sum(np.sin(15 * np.pi * x_normalized) * np.cos(15 * np.pi * x_normalized))
        
        # Cross-terms to increase dimensionality interaction
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:] * np.sin(4 * np.pi * x_normalized[:-1]))
        
        # Combine terms with different weights to create a challenging landscape
        return quadratic_term + 0.2 * sinusoidal_term + 0.1 * high_freq_term + 0.05 * cross_term