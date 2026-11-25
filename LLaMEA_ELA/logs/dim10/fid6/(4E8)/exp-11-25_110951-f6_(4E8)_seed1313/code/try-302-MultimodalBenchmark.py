import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal-like self-similarity with multi-scale sine-cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            term = np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            term += 0.5 * np.sin(5 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
            fractal += term * np.exp(-0.3 * x_norm[i]**2)
        
        # Enhanced log-periodic oscillations with dynamic frequency modulation
        log_osc = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(x_norm[i] * 0.5)
            log_osc += (np.sin(freq * 12 * x_norm[i]) * np.cos(freq * 9 * x_norm[i]) +
                       0.4 * np.sin(freq * 18 * x_norm[i])**2 * np.cos(freq * 14 * x_norm[i]))
        
        # Improved gradient-based attraction basins with asymmetric potentials
        gradient_attraction = 0.0
        for i in range(self.dim):
            # Create a landscape with multiple nested optima using asymmetric logarithmic potentials
            gradient_attraction += (np.log(1 + 0.4 * (x_norm[i] - 1)**2) +
                                  0.6 * np.log(1 + 0.2 * (x_norm[i] + 1)**2) +
                                  0.3 * np.log(1 + 0.1 * x_norm[i]**2) +
                                  0.2 * np.sin(4 * x_norm[i])**2)
        
        # Enhanced cross-dimensional interaction with modified exponential potentials
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_interaction += np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                               (np.sin(2.5 * x_norm[i]) * np.cos(2.5 * x_norm[j]) +
                                0.6 * np.sin(3.5 * x_norm[i]) * np.cos(3.5 * x_norm[j]))
        
        # Enhanced spectral harmonic interference with complex elliptic structures
        spectral_harmonic = 0.0
        for i in range(self.dim):
            spectral_harmonic += (np.sin(25 * x_norm[i]) * np.cos(22 * x_norm[i]) +
                                0.7 * np.sin(18 * x_norm[i])**3 * np.cos(15 * x_norm[i]))
        
        # Enhanced multi-scale sinusoidal modulations with adaptive weighting
        multi_scale = 0.0
        scales = [2, 3, 5, 7, 11, 13]
        for i in range(self.dim):
            for s in scales:
                multi_scale += np.sin(s * x_norm[i]) * np.cos(s * x_norm[i] / (s + 1)) * \
                              np.exp(-0.15 * (x_norm[i] - np.sin(x_norm[i]))**2) * \
                              (1 + 0.1 * np.cos(s * x_norm[i]))
        
        # Enhanced asymmetric elliptic structures with modified potentials
        elliptic_structure = 0.0
        for i in range(self.dim):
            elliptic_structure += (np.sin(6 * x_norm[i]) * np.cos(5 * x_norm[i]) +
                                0.4 * np.sin(9 * x_norm[i])**2 * np.cos(7 * x_norm[i]) +
                                0.3 * np.sin(12 * x_norm[i]) * np.cos(10 * x_norm[i]))
        
        # Dynamic weighting scheme with improved balance
        return (0.22 * fractal + 0.18 * log_osc + 0.17 * gradient_attraction + 
                0.12 * cross_interaction + 0.13 * spectral_harmonic + 
                0.1 * multi_scale + 0.08 * elliptic_structure)