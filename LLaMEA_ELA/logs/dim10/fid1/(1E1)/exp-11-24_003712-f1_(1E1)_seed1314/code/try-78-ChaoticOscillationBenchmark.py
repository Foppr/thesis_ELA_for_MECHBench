import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Radial basin term
        r_squared = np.sum(x**2, axis=1)
        radial_term = 0.01 * r_squared
        
        # Sinusoidal oscillation terms
        sin_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[:, i]) * np.cos(3.0 * x[:, i])
        
        # Cross-term interactions
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[:, i] * x[:, j]) * (i + j)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x[:, i] + np.sin(x[:, (i+1) % self.dim]))
        
        return radial_term + 0.5 * sin_term + 0.3 * cross_term + 0.2 * chaotic_term