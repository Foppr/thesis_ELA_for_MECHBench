import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic map
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic base using logistic map-like dynamics
        chaotic_base = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic-like chaotic map with parameter modulation
            xi_next = self.a * xi * (1 - xi) + self.b * np.sin(self.c * xi)
            chaotic_base += xi_next**2
        
        # Add periodic forcing terms with varying frequencies and amplitudes
        periodic_forcing = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Varying frequencies: 2, 4, 8, 16
            amp = 1.0 / (i + 1)
            periodic_forcing += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Saddle-point interaction terms with exponential decay
        saddle_interaction = 0.0
        for i in range(self.dim-1):
            diff = x_norm[i] - x_norm[i+1]
            prod = x_norm[i] * x_norm[i+1]
            saddle_interaction += (diff**2 + 0.5 * prod**2) * np.exp(-0.3 * (diff**2 + prod**2))
        
        # Mixed polynomial and trigonometric terms for additional complexity
        mixed_term = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                mixed_term += x_norm[i]**7 * np.cos(3 * x_norm[i])
            elif i % 4 == 1:
                mixed_term += x_norm[i]**4 * np.sin(2 * x_norm[i])
            elif i % 4 == 2:
                mixed_term += x_norm[i]**5 * np.tan(0.5 * x_norm[i])
            else:  # i % 4 == 3
                mixed_term += x_norm[i]**6 * np.exp(-x_norm[i]**2)
        
        # Combine all components with carefully tuned weights
        return 0.5 * chaotic_base + 0.3 * periodic_forcing + 0.2 * saddle_interaction + 0.1 * mixed_term