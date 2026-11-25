import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like self-similarity using recursive sine-cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            term = np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            fractal += term * np.exp(-0.5 * x_norm[i]**2)
        
        # Log-periodic oscillations with varying frequencies and amplitudes
        log_osc = 0.0
        for i in range(self.dim):
            freq = 1 + 0.5 * np.sin(x_norm[i])
            log_osc += (np.sin(freq * 10 * x_norm[i]) * np.cos(freq * 8 * x_norm[i]) +
                       0.3 * np.sin(freq * 15 * x_norm[i])**2 * np.cos(freq * 12 * x_norm[i]))
        
        # Gradient-based attraction basins with multiple local minima
        gradient_attraction = 0.0
        for i in range(self.dim):
            # Create a landscape with multiple nested optima
            gradient_attraction += (np.log(1 + 0.5 * (x_norm[i] - 1)**2) +
                                  0.7 * np.log(1 + 0.3 * (x_norm[i] + 1)**2) +
                                  0.4 * np.log(1 + 0.2 * x_norm[i]**2))
        
        # Cross-dimensional interaction with exponential potentials
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_interaction += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                               (np.sin(2 * x_norm[i]) * np.cos(2 * x_norm[j]) +
                                0.5 * np.sin(3 * x_norm[i]) * np.cos(3 * x_norm[j]))
        
        # Spectral harmonic interference with asymmetric elliptic structures
        spectral_harmonic = 0.0
        for i in range(self.dim):
            spectral_harmonic += (np.sin(20 * x_norm[i]) * np.cos(18 * x_norm[i]) +
                                0.6 * np.sin(15 * x_norm[i])**3 * np.cos(12 * x_norm[i]))
        
        # Multi-scale sinusoidal modulations with dynamic weighting
        multi_scale = 0.0
        scales = [2, 3, 5, 7, 11]
        for i in range(self.dim):
            for s in scales:
                multi_scale += np.sin(s * x_norm[i]) * np.cos(s * x_norm[i] / (s + 1)) * \
                              np.exp(-0.1 * (x_norm[i] - np.sin(x_norm[i]))**2)
        
        # Asymmetric elliptic structures with exponential potentials
        elliptic_structure = 0.0
        for i in range(self.dim):
            elliptic_structure += (np.sin(5 * x_norm[i]) * np.cos(4 * x_norm[i]) +
                                0.3 * np.sin(8 * x_norm[i])**2 * np.cos(6 * x_norm[i]))
        
        # Dynamic weighting scheme
        return (0.25 * fractal + 0.2 * log_osc + 0.15 * gradient_attraction + 
                0.1 * cross_interaction + 0.1 * spectral_harmonic + 
                0.1 * multi_scale + 0.05 * elliptic_structure)