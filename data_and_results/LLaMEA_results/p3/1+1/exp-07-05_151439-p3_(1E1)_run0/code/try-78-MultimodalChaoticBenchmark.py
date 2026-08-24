import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                        (1 + 0.3 * np.sin(np.sum(x**2)))) / self.dim
        
        # Polynomial with mixed even/odd powers and adaptive coefficients
        poly_mod = np.sum((1.5 + 0.2 * np.sin(self.dim)) * x**6 + 
                         (2.0 + 0.3 * np.cos(self.dim)) * x**5 + 
                         (1.8 + 0.25 * np.sin(self.dim)) * x**4 + 
                         (1.6 + 0.2 * np.cos(self.dim)) * x**3 + 
                         (1.4 + 0.15 * np.sin(self.dim)) * x**2 + 
                         (1.2 + 0.1 * np.cos(self.dim)) * x) / self.dim
        
        # Cross-dimensional interaction with dynamic coupling
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling = 1.5 + 0.4 * np.sin(i * 0.5 + self.dim * 0.3)
                cross_term += coupling * np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        cross_term /= (self.dim - 1)
        
        # Multiscale chaotic modulation with exponential decay
        chaotic_mod = np.sum(np.exp(-np.abs(x)) * np.sin(10 * x) * 
                           np.cos(5 * x) * np.sin(2 * x)) / self.dim
        
        # Adaptive noise component with dimensionality dependence
        noise = (0.02 * np.random.rand() + 
                0.01 * np.sin(np.sum(x)) * np.cos(np.sum(x**2)) + 
                0.005 * np.sin(self.dim) * np.cos(np.sum(x**3)) + 
                0.003 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)))
        
        # Combine all components with dynamic weights
        weights = [0.35 + 0.08 * np.sin(self.dim), 
                  0.30 + 0.07 * np.cos(self.dim), 
                  0.20 + 0.05 * np.sin(self.dim), 
                  0.15 + 0.04 * np.cos(self.dim)]
        
        result = (weights[0] * sin_mod + 
                 weights[1] * poly_mod + 
                 weights[2] * cross_term + 
                 weights[3] * chaotic_mod)
        
        return result + noise