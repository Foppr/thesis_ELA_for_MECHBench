import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial basin term
        basin_term = 0.01 * np.sum(x**4, axis=1)
        
        # Sinusoidal oscillation terms
        oscillation_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            oscillation_term += np.sin(5.0 * x[:, i]) * np.cos(3.0 * x[:, i])
        
        # Cross-term interactions
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[:, i] * x[:, j]) * (i + j)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x[:, i] + np.sin(x[:, (i+1) % self.dim])) * 0.5
        
        # Combine all terms with varying weights
        return basin_term + 2.0 * oscillation_term + 0.5 * cross_term + 0.3 * chaotic_term