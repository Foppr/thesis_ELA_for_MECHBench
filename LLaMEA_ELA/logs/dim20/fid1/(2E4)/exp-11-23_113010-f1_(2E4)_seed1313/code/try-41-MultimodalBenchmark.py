import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(17 * np.pi * x_norm[i]) * np.cos(9 * np.pi * x_norm[i])
        
        # Polynomial potential with modified degrees and weights
        poly_potential = np.sum(1.1 * x_norm**4 + 0.3 * x_norm**3 + 0.2 * x_norm**2)
        
        # Sinusoidal wave interference pattern with higher frequencies
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin(5 * np.pi * x_norm[i] * (i + 1)) * np.cos(6 * np.pi * x_norm[i] * (i + 1))
        
        # Enhanced cross-dimensional coupling with stronger interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-4*abs(x_norm[i] - x_norm[j])) * np.sin(4*np.pi * (x_norm[i] + x_norm[j]))
        
        # Modified saddle point structure with quartic terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**4 * np.cos(3 * np.pi * x_norm[i])
        
        # Add deterministic chaos scaling and noise
        noise = 0.02 * np.random.random()
        
        return 2.2 * chaotic + 0.7 * poly_potential + 0.9 * wave_sum + 0.7 * cross_coupling + 0.6 * saddle + noise