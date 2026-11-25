import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Radial basin term with chaotic modulation
        r_squared = np.sum(x**2, axis=1)
        radial_term = 0.01 * r_squared * (1.0 + 0.5 * np.sin(r_squared))
        
        # Sinusoidal oscillations in each dimension
        sin_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            sin_term += np.sin(x[:, i] * (i + 1) * np.pi / 2.0)
        
        # Cross-dimensional interactions
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[:, i] * x[:, j] * np.cos((i + j) * np.pi / 4.0)
        
        # Add chaotic component
        chaotic = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic += np.sin(x[:, i] * np.exp(i))
        
        return radial_term - 0.5 * sin_term + 0.1 * cross_term + 0.05 * chaotic