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
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_term += x[i]**2 * np.sin(10 * x[i])
            else:
                chaotic_term += (x[i] - x[i-1])**2 * np.cos(7 * x[i])
                
        # Cross-term interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * 0.1
                
        return poly_term + sin_term + chaotic_term + cross_term