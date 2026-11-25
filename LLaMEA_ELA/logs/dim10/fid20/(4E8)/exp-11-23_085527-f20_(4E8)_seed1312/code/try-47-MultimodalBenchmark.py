import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial conditioning with varying exponents
        polynomial = np.sum((x_scaled**2 + 0.1 * x_scaled**4) ** 2)
        
        # Sinusoidal oscillations with adaptive frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi / 2.0
            sinusoidal += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Cross-terms with adaptive weights based on dimensionality
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.1 * (i + j))
                cross_terms += weight * np.sin(x_scaled[i] * x_scaled[j]) * np.cos(x_scaled[i] + x_scaled[j])
        
        # Exponential decay with adaptive scaling
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                exponential += exp_decay * (x_scaled[i] - x_scaled[j])**2
        
        # Global minimum at origin with adaptive scaling
        return 3.0 * polynomial + 2.0 * sinusoidal + 1.5 * cross_terms + 1.0 * exponential