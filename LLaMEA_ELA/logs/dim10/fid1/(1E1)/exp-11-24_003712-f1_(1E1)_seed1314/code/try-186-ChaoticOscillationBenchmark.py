import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial basin term
        basin = np.sum(x**4, axis=1) * 0.01
        
        # Sinusoidal oscillation terms
        oscillation = np.zeros(x.shape[0])
        for i in range(self.dim):
            oscillation += np.sin(x[:, i] * np.pi * 2.0) * np.cos(x[:, i] * np.pi * 0.5)
        
        # Cross-term interactions
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[:, i] * x[:, j]) * (i + j) * 0.1
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic += np.sin(np.pi * x[:, i] * 3.0) * np.cos(np.pi * x[:, i] * 1.5)
        
        return basin + 0.5 * oscillation + 0.3 * cross_term + 0.2 * chaotic