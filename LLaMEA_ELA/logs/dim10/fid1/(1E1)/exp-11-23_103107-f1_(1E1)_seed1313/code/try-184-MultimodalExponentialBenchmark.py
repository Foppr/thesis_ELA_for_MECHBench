import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with fractional powers and dynamic phase shifts
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x)**1.7) * np.sin(2.5 * np.pi * x + 0.3 * np.sum(x))**3)
        
        # Nested trigonometric wave interactions with recursive frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                     np.cos(9 * x[i]) * np.sin(4 * x[i]) + 
                     np.sin(3 * x[i]) * np.cos(8 * x[i]) +
                     np.cos(6 * x[i]) * np.sin(2 * x[i])) * \
                    (1 + 0.3 * np.sin(0.7 * x[i])**2)
            
        # Complex cross-dimensional interactions with chaotic coupling and multi-scale effects
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j] * 0.5) * \
                                   np.cos(x[i] + x[j] * 0.3) * \
                                   (1 + 0.4 * np.sin(0.8 * (x[i] - x[j])**3)) * \
                                   (1 + 0.2 * np.cos(1.2 * (x[i] + x[j])**2))
                
        # Nested penalty regions with fractal-like structures and multiple local optima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.08 * (dist_from_origin - 2.5)**3)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 1.5)**3) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * (1 - np.exp(-0.05 * (dist_from_origin - 4)**2)) * \
                      np.sin(6 * np.pi * dist_from_origin)**2
        
        # Add global scaling and combine all components with chaotic mixing
        return 1.2 * (exp_decay + waves + cross_interactions + penalty) + \
               0.5 * np.sin(0.1 * np.sum(x**3)) * np.cos(0.1 * np.sum(x**4))