import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for the chaotic landscape
        self.c1 = 0.5
        self.c2 = 2.0
        self.c3 = 0.1
        self.c4 = 10.0
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Chaotic sinusoidal component
        chaotic_term = np.sum(np.sin(self.c1 * x) * np.cos(self.c2 * x), axis=1)
        
        # Exponential barrier terms to create fitness gradients
        barrier_term = np.sum(self.c3 * np.exp(self.c4 * (np.abs(x) - 4.5)), axis=1)
        
        # Additional oscillatory component with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        oscillation_term = np.sum(np.sin(freqs * x) * np.cos(freqs * x), axis=1)
        
        # Combine all terms with different weights
        result = 0.5 * chaotic_term + barrier_term + 0.3 * oscillation_term
        
        # Add a global quadratic term to ensure boundedness
        quadratic_term = 0.01 * np.sum(x**2, axis=1)
        
        return result + quadratic_term