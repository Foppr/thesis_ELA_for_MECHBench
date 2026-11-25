import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Radial basin term
        radial_term = np.sum(x**2, axis=1) / (2.0 * self.dim)
        
        # Sinusoidal oscillation component
        sin_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            sin_term += np.sin(3.0 * x[:, i]) * np.cos(2.0 * x[:, i])
        
        # Cross-term interactions
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[:, i] * x[:, j]) / (1.0 + np.abs(x[:, i]) + np.abs(x[:, j]))
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(np.pi * x[:, i] * np.sin(2.0 * np.pi * x[:, i]))
        
        # Combine all terms with varying weights
        return 0.3 * radial_term + 0.4 * sin_term + 0.2 * cross_term + 0.1 * chaotic_term