import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Radial basin term
        radial_term = np.sum(x**2, axis=1)
        
        # Sinusoidal oscillation terms
        sin_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[:, i]) * np.cos(3.0 * x[:, i])
        
        # Cross-terms creating non-separability
        cross_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[:, i] * x[:, j] * np.sin(2.0 * (x[:, i] + x[:, j]))
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x[:, i]) * np.cos(7.0 * x[:, i]) * np.exp(-0.1 * x[:, i]**2)
        
        # Combine all terms with different weights
        return 0.5 * radial_term + 2.0 * sin_term + 0.3 * cross_term + 0.1 * chaotic_term