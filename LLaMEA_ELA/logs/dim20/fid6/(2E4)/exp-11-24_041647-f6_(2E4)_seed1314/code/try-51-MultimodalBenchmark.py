import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term
        quadratic_term = 0.2 * np.sum(x_normalized**2)
        
        # Chaotic sinusoidal components with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 10 * (1.5 ** i)
            chaotic_term += np.sin(freq * x_normalized[i]) * np.exp(-0.5 * i) * (1 + 0.2 * x_normalized[i]**3)
        
        # Cross-dimensional interactions with coupling strength varying by dimension
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 * (1 - np.exp(-0.1 * (i + j)))
                cross_term += coupling * np.sin(8 * np.pi * x_normalized[i]) * np.cos(6 * np.pi * x_normalized[j])
        
        # Dynamic global minimum shift based on dimension
        shift = 0.3 * (self.dim / 10.0)
        shift_term = 0.8 * np.sum((x_normalized - shift)**3)
        
        return quadratic_term + chaotic_term + cross_term + shift_term