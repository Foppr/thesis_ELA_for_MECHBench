import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.c1 = 0.5
        self.c2 = 2.0
        self.c3 = 0.1
        self.noise_level = 0.05
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial basin term (quadratic + quartic)
        basin_term = np.sum(0.1 * x**2 + 0.01 * x**4, axis=1)
        
        # Sinusoidal waves with varying frequencies and amplitudes
        wave_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            # Chaotic frequency modulation
            freq = self.c1 * (i + 1) * (1.0 + 0.5 * np.sin(i * 0.7))
            amp = self.c2 * (1.0 + 0.3 * np.cos(i * 0.5))
            wave_term += amp * np.sin(freq * x[:, i])
        
        # Add chaotic component with exponential growth
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.exp(self.c3 * np.abs(x[:, i])) * np.cos(2.0 * x[:, i] + i)
        
        # Add random noise to increase irregularity
        noise = self.noise_level * np.random.randn(x.shape[0])
        
        # Combine all terms with different weights
        return basin_term + 0.3 * wave_term + 0.2 * chaotic_term + noise