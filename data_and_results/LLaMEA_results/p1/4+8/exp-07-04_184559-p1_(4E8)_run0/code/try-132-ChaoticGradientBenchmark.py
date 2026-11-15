import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using logistic map for dynamic conditioning
        chaotic_factor = 1.0
        for i in range(5):
            chaotic_factor = 4.0 * chaotic_factor * (1.0 - chaotic_factor)
        
        # Adaptive conditioning based on dimensionality and chaos
        condition = 1.0 + 0.5 * np.sin(self.dim) * chaotic_factor
        
        # Sinusoidal perturbations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(condition * x_norm) * np.cos(2 * condition * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Quadratic base with adaptive scaling
        quad_base = np.sum(condition * x_norm**2)
        
        # Saddle-point dominant structure with cross-terms
        saddle = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                saddle += (x_norm[i]**2 - x_norm[i+1]**2) * np.sin(3 * x_norm[i] * x_norm[i+1])
        
        # High-frequency oscillation component for increased complexity
        high_freq = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.05 * np.sum(x_norm**2)))
        
        # Combined fitness with weighted components
        return quad_base + 0.5 * sin_term + 0.3 * saddle + 0.2 * high_freq