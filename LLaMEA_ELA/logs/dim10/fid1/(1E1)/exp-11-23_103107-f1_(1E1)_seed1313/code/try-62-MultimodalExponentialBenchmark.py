import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with varying decay rates and phase shifts
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.7)**3)
        
        # Enhanced trigonometric wave interactions with chaotic frequencies and coupling
        waves = 0
        for i in range(self.dim):
            waves += np.sin(6 * x[i]) * np.cos(7 * x[i]) + \
                    np.cos(9 * x[i]) * np.sin(4 * x[i]) + \
                    np.sin(3 * x[i]) * np.cos(10 * x[i]) + \
                    np.cos(5 * x[i]) * np.sin(8 * x[i])
            
        # Chaotic cross-dimensional interactions with non-linear coupling and multiple saddle points
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j] + 0.5) * np.cos(x[i] + x[j] + 0.3) * \
                                   (1 + 0.7 * np.sin(0.8 * (x[i] - x[j])**3)) * \
                                   np.tanh(0.2 * (x[i]**2 - x[j]**2))
                
        # Complex nested penalty regions with multiple local minima and chaotic scaling
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.1 * (dist_from_origin - 4)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.exp(-0.05 * (dist_from_origin - 3.5)**2) * \
                      np.sin(6 * np.pi * dist_from_origin)**2
        
        # Add a global scaling factor and combine all components
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)