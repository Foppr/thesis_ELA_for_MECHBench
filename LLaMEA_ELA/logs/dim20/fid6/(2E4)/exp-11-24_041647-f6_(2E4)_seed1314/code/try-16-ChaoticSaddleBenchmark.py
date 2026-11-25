import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay interaction terms
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-0.5 * np.sum((x_normalized - x_normalized[i])**2)) * (1 + 0.1 * np.sin(3 * np.pi * x_normalized[i]))
        
        # Sinusoidal modulation with non-uniform frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3)  # Varying frequencies: 1, 2, 4
            sin_mod += np.sin(freq * np.pi * x_normalized[i]) * np.cos(0.5 * np.pi * x_normalized[i]**2)
        
        # Chaotic saddle point with polynomial and exponential components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_normalized[i]**4 - 2 * x_normalized[i]**2 + 0.5) * np.exp(-0.1 * np.sum(x_normalized**2))
        
        # Asymmetric penalty for boundary behavior
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 10 * (np.abs(x_normalized[i]) > 0.9) * np.exp(5 * (np.abs(x_normalized[i]) - 0.9))
        
        return exp_term + sin_mod + saddle_term + boundary_penalty