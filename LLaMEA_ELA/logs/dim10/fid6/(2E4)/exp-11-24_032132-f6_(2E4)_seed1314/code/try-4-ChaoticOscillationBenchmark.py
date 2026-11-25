import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basin term
        radial_term = np.sum(x_norm**2)
        
        # Sinusoidal oscillation components
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
            
        # Cross-term interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_norm[i] * x_norm[j]) * (i + j)
                
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(20 * np.sin(x_norm[i])) * np.cos(15 * np.sin(x_norm[i]))
            
        return radial_term + 0.5 * sin_sum + 0.1 * cross_term + 0.3 * chaotic