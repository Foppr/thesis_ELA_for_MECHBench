import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic_term = np.sum(np.sin(2 * np.pi * x_norm * (1 + 0.5 * np.abs(x_norm))) * 
                              np.cos(3 * np.pi * x_norm * (1 + 0.3 * np.abs(x_norm))) * 
                              (1 + 0.2 * np.sin(x_norm * 7)))
        
        # Radial basin with adaptive scaling based on dimensionality
        radial_term = np.sum((x_norm ** 2) * (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.0 / (1.0 + 0.1 * (i + j))
                interaction = np.sin(coupling_strength * x_norm[i] * x_norm[j]) * \
                             np.cos(coupling_strength * (x_norm[i]**2 + x_norm[j]**2))
                interaction_term += interaction
        
        # Adaptive noise-like modulation based on position and dimension
        noise_term = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 3) * (1 + 0.2 * np.sin(i * 0.5))
            amp = 1.0 / (1.0 + 0.2 * i)
            noise_term += amp * np.sin(freq * x_norm[i] + i * 0.3) * \
                         np.cos(freq * x_norm[i] * 0.7 + i * 0.4)
        
        # Combine all terms with weighted contributions
        return (0.35 * periodic_term + 
                0.25 * radial_term + 
                0.20 * interaction_term + 
                0.20 * noise_term)