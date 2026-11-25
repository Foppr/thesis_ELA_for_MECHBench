import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial basin term
        basin_term = np.sum(x**4, axis=1) * 0.01
        
        # Sinusoidal oscillation term with varying frequencies
        oscillation_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            oscillation_term += np.sin(x[:, i] * (i + 1) * 2 * np.pi / 5.0) * np.cos(x[:, i] * (i + 1) * 3 * np.pi / 5.0)
        
        # Cross-term interaction
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[:, i] * x[:, j] * np.sin((i + j) * np.pi / 4.0)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(x[:, i] * 10.0) * np.cos(x[:, i] * 7.0) * np.exp(-np.abs(x[:, i]) / 5.0)
        
        return basin_term + 0.5 * oscillation_term + 0.3 * cross_term + 0.2 * chaotic_term