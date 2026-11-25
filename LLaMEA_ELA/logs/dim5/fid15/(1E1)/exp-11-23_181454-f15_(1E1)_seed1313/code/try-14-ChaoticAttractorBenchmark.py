import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Central attractive force term
        center_force = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillations with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Different frequencies for different dimensions
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Chaotic component with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-abs(x[i])) * np.sin(10 * x[i])
        
        # Combine terms with different weights
        return center_force + 0.5 * sin_term + 0.3 * chaotic_term