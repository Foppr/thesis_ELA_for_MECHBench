import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with fractal-like behavior and varying decay rates
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.3)**3 + 
                          0.5 * np.exp(-0.2 * x**2) * np.cos(7 * np.pi * x + 0.7)**2)
        
        # Augmented trigonometric wave interactions with non-linear coupling and phase modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i]) + 
                     np.cos(6 * x[i]) * np.sin(3 * x[i]) * np.cos(9 * x[i]) + 
                     np.sin(8 * x[i]) * np.cos(5 * x[i]) * np.sin(7 * x[i]))
            
        # Complex cross-dimensional interactions with chaotic coupling and nested exponential terms
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j] + 0.5) * np.cos(x[i] + x[j] + 0.3) * \
                                   (1 + 0.3 * np.sin(0.7 * (x[i] - x[j])**3)) * \
                                   np.exp(-0.1 * np.abs(x[i] - x[j]))
                
        # Complex penalty regions with nested local minima, chaotic oscillations, and multi-scale effects
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 4)**2)) * \
                      np.sin(5 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 2)**2) * \
                      np.cos(6 * np.pi * dist_from_origin)**3 + \
                      5 * np.sin(4 * dist_from_origin) * np.cos(8 * dist_from_origin)
        
        # Add a global scaling factor and combine all components with enhanced non-linearity
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)