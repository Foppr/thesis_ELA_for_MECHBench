import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with high-order terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**6 - 15*x[i]**4 + 75*x[i]**2 - 125) * np.sin(x[i])
        poly_chaos /= self.dim
        
        # Sinusoidal radial interactions with varying frequencies
        radius = np.sqrt(np.sum(x**2))
        sin_radial = np.sin(3 * radius) * np.cos(5 * radius) * np.exp(-radius / 4)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-abs(x[i] - x[j]) / 3)
        cross_coupling /= (self.dim * (self.dim - 1) / 2)
        
        # Multi-scale chaotic modulation with exponential decay
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.exp(-x[i]**2 / 3) + \
                          np.sin(7 * x[i]) * np.cos(12 * x[i]) * np.exp(-x[i]**2 / 2)
        chaotic_mod /= self.dim
        
        # Nested exponential decay with sinusoidal perturbations
        nested_exp = 0.0
        for i in range(self.dim):
            nested_exp += np.exp(-abs(x[i])**3) * np.sin(4 * x[i]) + \
                         np.exp(-abs(x[i])**2) * np.cos(6 * x[i])
        nested_exp /= self.dim
        
        # Combine all components with different weights
        result = (poly_chaos * 0.7 + sin_radial * 0.5 + 
                 cross_coupling * 0.6 + chaotic_mod * 0.4 + nested_exp * 0.3)
        
        return float(result)