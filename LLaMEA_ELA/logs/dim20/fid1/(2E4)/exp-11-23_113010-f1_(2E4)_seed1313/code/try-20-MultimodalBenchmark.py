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
            chaotic += np.sin(10 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i])
        
        # Polynomial potential with mixed degrees
        poly_potential = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Sinusoidal wave interference pattern
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin(2 * np.pi * x_norm[i] * (i + 1)) * np.cos(3 * np.pi * x_norm[i] * (i + 1))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-abs(x_norm[i] - x_norm[j])) * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle point structure
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**2 * np.cos(4 * np.pi * x_norm[i])
        
        # Add deterministic chaos scaling and noise
        noise = 0.02 * np.random.random()
        
        return 1.5 * chaotic + 0.7 * poly_potential + 0.6 * wave_sum + 0.4 * cross_coupling + 0.3 * saddle + noise