import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term
        quadratic_term = 0.2 * np.sum(x_normalized**2)
        
        # Chaotic sinusoidal components with modified exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 12 * (1.3 ** i)
            chaotic_term += np.sin(freq * x_normalized[i]) * np.exp(-0.3 * i) * (1 + 0.15 * x_normalized[i]**4)
        
        # Cross-dimensional interactions with modified coupling strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.7 * (1 - np.exp(-0.15 * (i + j)))
                cross_term += coupling * np.sin(6 * np.pi * x_normalized[i]) * np.cos(4 * np.pi * x_normalized[j])
        
        # Perturbed global minimum shift based on dimension
        shift = 0.2 * (self.dim / 8.0)
        shift_term = 1.0 * np.sum((x_normalized - shift)**4)
        
        return quadratic_term + chaotic_term + cross_term + shift_term