import numpy as np

class WaveGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters for each dimension
        self.wave_freq = np.random.uniform(1.0, 3.0, dim)
        self.wave_amp = np.random.uniform(0.5, 2.0, dim)
        self.gauss_centers = np.random.uniform(-2.0, 2.0, (5, dim))
        self.gauss_stds = np.random.uniform(0.3, 1.0, (5, dim))
        self.gauss_weights = np.random.uniform(0.5, 2.0, 5)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Wave interference component
        wave = np.zeros_like(x_scaled)
        for i in range(self.dim):
            wave += self.wave_amp[i] * np.sin(self.wave_freq[i] * x_scaled[i]) * \
                   np.cos(self.wave_freq[i] * x_scaled[i] * 0.7)
        
        # Gaussian mixture component
        gauss = np.zeros_like(x_scaled)
        for i in range(5):
            g = self.gauss_weights[i]
            for j in range(self.dim):
                g *= np.exp(-0.5 * ((x_scaled[j] - self.gauss_centers[i, j]) / self.gauss_stds[i, j])**2)
            gauss += g
        
        # Adaptive penalty based on proximity to known good solutions
        penalty = 0.0
        for i in range(5):
            dist = np.sum((x_scaled - self.gauss_centers[i])**2)
            if dist < 0.1:
                penalty += 10.0 * np.exp(-dist * 50.0)
        
        # Cross-dimensional interaction with periodic modulation
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                mod = np.sin(2.0 * (x_scaled[i] + x_scaled[j]))
                interaction += mod * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Return combined function value with dynamic scaling
        return 1.5 * np.sum(wave**2) + 0.8 * gauss + 0.3 * interaction + penalty