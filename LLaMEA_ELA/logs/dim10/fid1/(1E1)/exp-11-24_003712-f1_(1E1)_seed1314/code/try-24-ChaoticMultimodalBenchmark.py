import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.freqs = 2 * np.pi * np.arange(1, dim + 1) / dim
        self.amp_factors = 1.0 + 0.5 * np.sin(np.arange(1, dim + 1))
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
            
        # Radial basin term
        radial = np.sum(x**2, axis=1)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(
            self.amp_factors * np.sin(self.freqs * x) * 
            np.cos(self.freqs * x), 
            axis=1
        )
        
        # Cross-dimensional interaction terms
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * x[:, i] * x[:, j] * np.sin(0.5 * (x[:, i] + x[:, j]))
        
        # Chaotic modulation based on radial distance
        chaotic_mod = 1.0 + 0.3 * np.sin(3.0 * np.sqrt(radial))
        
        return chaotic_mod * (0.5 * radial + 0.3 * sin_term + 0.2 * cross_term)