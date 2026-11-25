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
            chaotic += np.sin(15 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
        
        # Polynomial potential with modified degrees and weights
        poly_potential = np.sum(0.9 * x_norm**4 + 0.25 * x_norm**3 + 0.15 * x_norm**2)
        
        # Sinusoidal wave interference pattern with higher frequencies
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin(4 * np.pi * x_norm[i] * (i + 1)) * np.cos(5 * np.pi * x_norm[i] * (i + 1))
        
        # Enhanced cross-dimensional coupling with stronger interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-3*abs(x_norm[i] - x_norm[j])) * np.sin(3*np.pi * (x_norm[i] + x_norm[j]))
        
        # Modified saddle point structure with quartic terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**4 * np.cos(2 * np.pi * x_norm[i])
        
        # Add deterministic chaos scaling and noise
        noise = 0.018 * np.random.random()
        
        return 2.0 * chaotic + 0.6 * poly_potential + 0.8 * wave_sum + 0.6 * cross_coupling + 0.5 * saddle + noise