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
            oscillation_term += np.sin(x[:, i] * (i + 1)) * np.cos(x[:, i] * (i + 1) * 0.5)
        
        # Cross-term interaction
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[:, i] * x[:, j]) * (i + j) * 0.1
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(np.pi * x[:, i] * np.sin(x[:, i])) * 0.5
            
        return basin_term + oscillation_term + cross_term + chaotic_term