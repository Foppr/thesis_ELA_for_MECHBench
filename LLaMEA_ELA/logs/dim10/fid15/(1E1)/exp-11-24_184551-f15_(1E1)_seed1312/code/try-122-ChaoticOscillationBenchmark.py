import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial potential term
        poly_term = np.sum(x**4) * 0.01
        
        # Sinusoidal oscillation term with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_term += (4.0 * x[i] * (1.0 - x[i])) ** 2
            else:
                chaotic_term += (4.0 * x[i] * (1.0 - x[i]) + 0.1 * x[i-1]) ** 2
        
        # Cross-term interaction
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += x[i] * x[i+1] * np.sin(x[i] + x[i+1])
        
        # Add noise
        noise = np.random.normal(0, 0.01)
        
        return poly_term + sin_term + chaotic_term + cross_term + noise