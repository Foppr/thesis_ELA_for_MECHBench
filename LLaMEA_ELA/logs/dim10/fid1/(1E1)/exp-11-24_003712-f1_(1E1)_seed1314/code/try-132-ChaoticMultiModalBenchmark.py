import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 2.0
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Sinusoidal wave component with varying frequencies
        wave_term = np.sum(np.sin(self.a * x) * np.cos(self.b * x**2), axis=1)
        
        # Polynomial penalty for staying near boundaries
        penalty = np.sum(np.where(np.abs(x) > 4.0, (np.abs(x) - 4.0)**3, 0.0), axis=1)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(x[:, i] * np.pi / 2.0) * np.cos(x[:, (i + 1) % self.dim] * np.pi / 3.0)
        
        # Combine all components with different weights
        return 0.5 * wave_term + 0.3 * chaotic_term + 0.2 * penalty