import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Exponentially decaying sinusoidal waves with varying frequencies
        f2 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi * x_norm)
        f3 = np.sum(condition_factor * np.sin(5 * np.pi * x_norm**2) * np.cos(3 * np.pi * x_norm**3))
        
        # Chaotic interaction using logistic map-like dynamics
        chaotic_term = np.zeros_like(x_norm)
        r = 3.9  # Chaos parameter
        for i in range(len(x_norm)):
            if i == 0:
                chaotic_term[i] = x_norm[i]
            else:
                chaotic_term[i] = r * chaotic_term[i-1] * (1 - chaotic_term[i-1])
        f4 = np.sum(chaotic_term * np.sin(2 * np.pi * x_norm))
        
        # Multi-scale periodicity with amplitude modulation
        f5 = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * (1 + 0.2 * np.sin(8 * x_norm)))
        
        # Non-separable interaction using a custom polynomial kernel
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i] - x_norm[j])**4 + np.sin(x_norm[i] + x_norm[j])
        f6 = interaction
        
        # Combine all terms with dynamic weights based on dimensionality
        weight1 = 0.4 + 0.1 * np.sin(0.5 * self.dim)
        weight2 = 0.3 + 0.05 * np.cos(0.3 * self.dim)
        weight3 = 0.2 + 0.08 * np.sin(0.7 * self.dim)
        weight4 = 0.1 + 0.03 * np.cos(0.4 * self.dim)
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + 0.05 * f5 + 0.02 * f6