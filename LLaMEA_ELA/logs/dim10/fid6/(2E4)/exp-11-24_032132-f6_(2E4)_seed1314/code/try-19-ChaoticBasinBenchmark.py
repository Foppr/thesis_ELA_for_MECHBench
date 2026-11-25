import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.coefficients = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Radial basin term
        radial_term = np.sum(x**2) * 0.1
        
        # Sinusoidal oscillations with different frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.coefficients[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += np.sin(x[i] * x[i+1]) * (x[i]**2 + x[i+1]**2)
        
        # Add a global minimum at the origin with additional penalty
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i] - 0.1)**2
        
        return radial_term + sin_term + chaotic_term + penalty * 0.5