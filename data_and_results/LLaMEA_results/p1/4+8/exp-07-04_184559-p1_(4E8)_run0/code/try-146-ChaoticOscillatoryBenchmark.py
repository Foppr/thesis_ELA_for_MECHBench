import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillatory component with varying frequencies and amplitudes
        oscillatory = np.sum(np.sin(7 * x_norm) * np.cos(5 * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Polynomial chaos component with higher-order terms and adaptive weights
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += (x_norm[i]**3 + 0.5 * x_norm[i]**4 + 0.2 * x_norm[i]**5) * np.cos(2 * np.pi * i / self.dim)
        
        # Adaptive conditioning based on dimensionality and chaotic perturbations
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1 + 0.3 * np.sin(13 * x_norm[i])) * (x_norm[i]**2 + 0.1 * x_norm[i]**6)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_interaction += np.sin(3 * x_norm[i]) * np.cos(4 * x_norm[j]) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Multi-scale sinusoidal modulation with dynamic phase shifts
        multi_scale = 0.0
        for k in range(1, 6):
            multi_scale += np.sin(k * np.pi * np.sum(x_norm)) * np.cos(k * np.pi * np.sum(x_norm**2))
        
        # Logarithmic penalty term with chaotic modulation
        log_penalty = np.sum(np.log(1 + 0.5 * x_norm**2) * np.sin(11 * x_norm))
        
        # Combine all components with dynamic weights based on dimension
        weight_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return weight_factor * (oscillatory + 0.7 * polynomial + 0.5 * conditioning + 0.3 * cross_interaction + 0.2 * multi_scale + 0.1 * log_penalty)