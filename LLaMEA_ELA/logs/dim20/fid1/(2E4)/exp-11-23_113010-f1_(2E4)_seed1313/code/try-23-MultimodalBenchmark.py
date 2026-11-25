import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using logistic map-like behavior with higher frequency
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
        
        # Polynomial potential with mixed degrees and higher order terms
        poly_potential = np.sum(x_norm**6 + 0.7 * x_norm**5 + 0.4 * x_norm**4 + 0.2 * x_norm**3)
        
        # Sinusoidal wave interference pattern with more complex interaction
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin(3 * np.pi * x_norm[i] * (i + 1)) * np.cos(4 * np.pi * x_norm[i] * (i + 1))
        
        # Enhanced cross-dimensional coupling with nonlinear interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle point structure with higher-order terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**3 * np.cos(5 * np.pi * x_norm[i])
        
        # Add deterministic chaos scaling and noise with adaptive amplitude
        noise = 0.03 * np.random.random()
        
        return 2.0 * chaotic + 0.8 * poly_potential + 0.7 * wave_sum + 0.5 * cross_coupling + 0.4 * saddle + noise