import numpy as np

class ExponentialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical harmonic-like interaction terms
        harmonic_sum = 0.0
        for i in range(1, min(4, self.dim + 1)):
            for j in range(i+1, min(6, self.dim + 1)):
                harmonic_sum += np.sin(i * x_norm[i-1]) * np.cos(j * x_norm[j-1])
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.5 * (x_norm**2)) * (1.0 + 0.1 * np.abs(x_norm)))
        
        # Adaptive noise component based on dimensionality
        noise = 0.01 * np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        # Cross-dimensional coupling with exponential weights
        coupling = 0.05 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Quadratic base with dimension-dependent scaling
        quadratic = 0.5 * np.sum(x_norm**2) * (1.0 + 0.1 * self.dim)
        
        # Combine all components
        return quadratic + harmonic_sum + exp_decay + noise + coupling