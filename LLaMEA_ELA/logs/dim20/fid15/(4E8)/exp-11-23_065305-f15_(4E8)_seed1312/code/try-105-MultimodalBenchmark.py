import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential radial decay component
        radius = np.sqrt(np.sum(x**2))
        exp_decay = np.exp(-radius / 3) * np.sin(2 * radius) * np.cos(4 * radius)
        
        # Trigonometric cross-dimensional interactions with altered weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i]) * np.cos(x[j]) * np.exp(-abs(x[i] - x[j]) / 2)
        cross_term /= (self.dim * (self.dim - 1) / 2)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(3 * x[i]) * np.cos(7 * x[i]) + 
                           np.sin(5 * x[i]) * np.cos(9 * x[i]) +
                           np.sin(2 * x[i]) * np.cos(6 * x[i]))
        multi_scale /= self.dim
        
        # Nested chaotic structure with polynomial and exponential components
        nested = 0.0
        for i in range(self.dim):
            nested += (np.sin(15 * x[i]) * np.cos(12 * x[i]) + 
                      0.5 * np.exp(-x[i]**2) * np.sin(8 * x[i]))
        nested /= self.dim
        
        # Add a chaotic perturbation term with high frequency oscillations
        chaos_perturb = 0.0
        for i in range(self.dim):
            chaos_perturb += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-x[i]**2 / 2)
        chaos_perturb /= self.dim
        
        # Add chaotic radial basis function component with shifted global minimum
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-((x[i] - 1.0)**2 + (x[(i+1) % self.dim] - 1.0)**2) / 2)
        rbf_component /= self.dim
        
        # Combine all components with different weights
        result = (exp_decay * 0.8 + cross_term * 0.6 + 
                 multi_scale * 0.7 + nested * 0.5 + chaos_perturb * 0.3 + rbf_component * 0.4)
        
        return float(result)