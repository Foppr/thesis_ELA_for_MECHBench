import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.chaos_factor = 0.5
        self.noise_level = 0.1
        self.polynomial_degree = 4
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial basin term
        poly_term = np.sum((x / 5.0)**self.polynomial_degree, axis=1)
        
        # Sinusoidal wave components with chaotic frequencies
        sin_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * (1 + self.chaos_factor * np.sin(i))
            sin_term += np.sin(freq * x[:, i]) * np.cos(freq * x[:, i])
        
        # Add random noise
        noise = np.random.normal(0, self.noise_level, x.shape[0])
        
        # Combine all terms with different weights
        return 0.3 * poly_term + 0.4 * sin_term + 0.3 * noise