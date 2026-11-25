import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.c1 = 0.5
        self.c2 = 2.0
        self.c3 = 0.1
        self.c4 = 3.0
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial valley term
        valley_term = np.sum((x**2), axis=1)
        
        # Sinusoidal oscillation term with chaotic behavior
        oscillation_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            # Chaotic sinusoidal component with varying frequencies
            freq = self.c1 * (i + 1) + np.sin(i * self.c2)
            oscillation_term += np.sin(freq * x[:, i]) * np.cos(freq * x[:, i])
        
        # Add chaotic modulation based on position
        chaotic_modulation = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_modulation += np.sin(self.c3 * x[:, i] + self.c4 * np.cos(x[:, (i+1) % self.dim]))
        
        # Combine all terms with different weights
        return 0.5 * valley_term + 0.3 * oscillation_term + 0.2 * chaotic_modulation