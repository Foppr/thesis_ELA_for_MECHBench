import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial radial decay component
        radius = np.sqrt(np.sum(x**2))
        poly_decay = (1.0 + 0.5 * radius) * np.exp(-radius / 4) * np.sin(3 * radius) * np.cos(5 * radius)
        
        # Trigonometric cross-dimensional interactions with varying weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-abs(x[i] - x[j]) / 3)
        cross_term /= (self.dim * (self.dim - 1) / 2)
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(4 * x[i]) * np.cos(8 * x[i]) + 
                           np.sin(6 * x[i]) * np.cos(10 * x[i]) +
                           np.sin(3 * x[i]) * np.cos(7 * x[i]))
        multi_scale /= self.dim
        
        # Nested chaotic structure with polynomial and exponential components
        nested = 0.0
        for i in range(self.dim):
            nested += (np.sin(20 * x[i]) * np.cos(15 * x[i]) + 
                      0.3 * np.exp(-x[i]**2) * np.sin(12 * x[i]))
        nested /= self.dim
        
        # Add a chaotic perturbation term with high frequency oscillations
        chaos_perturb = 0.0
        for i in range(self.dim):
            chaos_perturb += np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.exp(-x[i]**2 / 3)
        chaos_perturb /= self.dim
        
        # Combine all components with different weights
        result = (poly_decay * 0.7 + cross_term * 0.5 + 
                 multi_scale * 0.6 + nested * 0.4 + chaos_perturb * 0.2)
        
        return float(result)