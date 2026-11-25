import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay modulation with chaotic base
        exp_mod = np.exp(-np.sum(x_normalized**2) / (2 * self.dim))
        
        # Multi-scale sinusoidal interference with varying frequencies
        sin_sum = 0.0
        for i in range(1, min(6, self.dim + 1)):
            sin_sum += np.sin(i * np.pi * x_normalized) * np.cos(i * np.pi * x_normalized)
        
        # Chaotic gradient component using logistic map-like dynamics
        chaotic_grad = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_grad += np.sin(3 * x_normalized[i]) * np.exp(-x_normalized[i]**2)
            else:
                chaotic_grad += np.sin(2 * x_normalized[i] + np.sin(x_normalized[i-1])) * np.cos(x_normalized[i])
        
        # Adaptive conditioning factor
        cond_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-0.5 * (x_normalized[i] - x_normalized[i+1])**2) * np.sin(2 * np.pi * (x_normalized[i] + x_normalized[i+1]))
        
        # Final combined landscape
        return cond_factor * (exp_mod * sin_sum + chaotic_grad + cross_coupling)