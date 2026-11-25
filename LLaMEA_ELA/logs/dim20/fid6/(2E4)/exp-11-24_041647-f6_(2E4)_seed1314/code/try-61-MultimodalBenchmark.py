import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term with adaptive weighting
        quadratic_term = 0.3 * np.sum(x_normalized**2)
        
        # Enhanced chaotic sinusoidal components with variable decay rates
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 15 * (1.4 ** i)
            decay = 0.25 * (1 + 0.2 * np.sin(i))
            chaotic_term += np.sin(freq * x_normalized[i]) * np.exp(-decay * i) * (1 + 0.2 * x_normalized[i]**3)
        
        # Cross-dimensional interactions with dynamic coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.8 * (1 - np.exp(-0.2 * (i + j)))
                cross_term += coupling * np.sin(8 * np.pi * x_normalized[i]) * np.cos(5 * np.pi * x_normalized[j])
        
        # Perturbed global minimum shift with dimension-dependent modulation
        shift = 0.25 * (self.dim / 10.0)
        shift_term = 1.2 * np.sum((x_normalized - shift)**3)
        
        # Additional high-frequency oscillation component
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += np.sin(20 * x_normalized[i]) * np.cos(15 * x_normalized[i]) * (1 + 0.1 * np.abs(x_normalized[i]))
        
        return quadratic_term + chaotic_term + cross_term + shift_term + high_freq_term