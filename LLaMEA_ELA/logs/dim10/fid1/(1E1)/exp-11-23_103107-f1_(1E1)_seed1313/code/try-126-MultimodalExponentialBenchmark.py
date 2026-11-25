import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Enhanced exponential decay terms with varying rates and phase shifts
        exp_decay = np.sum(np.exp(-0.2 * x**2) * np.sin(3 * np.pi * x + 0.5)**2)
        
        # Modified trigonometric wave interactions with different frequencies and coupling
        waves = 0
        for i in range(self.dim):
            waves += np.sin(4 * x[i]) * np.cos(6 * x[i]) + \
                    np.cos(8 * x[i]) * np.sin(3 * x[i]) + \
                    np.sin(2 * x[i]) * np.cos(9 * x[i])
            
        # Enhanced cross-dimensional interactions with stronger coupling and additional terms
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                                   (1 + 0.3 * np.sin(0.5 * (x[i] - x[j])**2))
                
        # Refined spherical penalty regions with multiple local minima and varied scales
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 12 * (1 - np.exp(-0.08 * (dist_from_origin - 3)**2)) * \
                      np.sin(3 * np.pi * dist_from_origin)**2 + \
                      7 * np.exp(-0.15 * (dist_from_origin - 1)**2) * \
                      np.cos(4 * np.pi * dist_from_origin)**2
        
        # Add a global scaling factor and combine all components
        return 0.85 * (exp_decay + waves + cross_interactions + penalty)