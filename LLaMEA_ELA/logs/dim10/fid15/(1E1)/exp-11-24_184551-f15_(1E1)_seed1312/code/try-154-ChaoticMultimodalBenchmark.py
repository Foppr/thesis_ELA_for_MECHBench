import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal base with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(2 * np.pi * x[i]) * np.sin(3 * np.pi * x[i])
        
        # Polynomial penalty for staying away from boundaries
        penalty = 0.0
        for i in range(self.dim):
            penalty += (abs(x[i]) - 5.0)**4
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(np.pi * x[i] * np.cos(x[i]))
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x[i] - x[j])**2 * np.sin(x[i] + x[j])
        
        return sin_term + penalty + chaotic + interaction