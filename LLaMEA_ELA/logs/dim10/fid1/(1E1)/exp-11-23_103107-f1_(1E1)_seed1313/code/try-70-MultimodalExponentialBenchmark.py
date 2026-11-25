import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Enhanced exponential decay terms with chaotic phase shifts and varying rates
        exp_decay = np.sum(np.exp(-0.4 * x**2) * np.sin(5 * np.pi * x + 0.7 * np.sin(2 * x))**3)
        
        # Chaotic trigonometric wave interactions with non-linear coupling and frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                     np.cos(9 * x[i]) * np.sin(4 * x[i]) + 
                     np.sin(3 * x[i]) * np.cos(8 * x[i]) +
                     np.sin(6 * x[i]) * np.cos(5 * x[i]) * np.sin(2 * x[i]))
            
        # Chaotic cross-dimensional interactions with fractional powers and nested coupling
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                                   (1 + 0.3 * np.sin(0.7 * (x[i] - x[j])**3)) * \
                                   (1 + 0.2 * np.cos(0.4 * (x[i]**2 + x[j]**2)))
                
        # Complex nested penalty regions with multiple scales and chaotic minima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.08 * (dist_from_origin - 2.5)**3)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 1.2)**3) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.sin(0.5 * dist_from_origin)**4 * \
                      np.cos(3 * np.pi * dist_from_origin)**2
        
        # Add chaotic global scaling and combine all components
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)