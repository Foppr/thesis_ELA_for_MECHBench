import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with varying decay rates and phase shifts
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.7)**3)
        
        # Nested trigonometric wave interactions with fractal-like frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                     np.cos(9 * x[i]) * np.sin(4 * x[i]) + 
                     np.sin(3 * x[i]) * np.cos(10 * x[i]) +
                     np.cos(6 * x[i]) * np.sin(8 * x[i]))
            
        # Fractal-like cross-dimensional interactions with recursive coupling
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                                   np.sin(0.5 * (x[i] - x[j])**3) * \
                                   (1 + 0.3 * np.sin(2 * x[i] * x[j]))
                
        # Nested penalty regions with self-similar structures and multiple local minima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 4)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.exp(-0.08 * (dist_from_origin - 3.5)**2) * \
                      np.sin(6 * np.pi * dist_from_origin)**2
        
        # Add global scaling factor and combine all components
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)