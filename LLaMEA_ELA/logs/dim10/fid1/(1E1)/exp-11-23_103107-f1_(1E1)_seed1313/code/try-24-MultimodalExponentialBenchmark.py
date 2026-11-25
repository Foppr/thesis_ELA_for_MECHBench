import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.3 * x**2) * np.sin(2.5 * np.pi * x)**2)
        
        # Trigonometric wave interactions with different frequencies
        waves = 0
        for i in range(self.dim):
            waves += np.sin(3.5 * x[i]) * np.cos(5.5 * x[i]) + \
                    np.cos(7.5 * x[i]) * np.sin(4.5 * x[i])
            
        # Cross-dimensional interactions with exponential coupling
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(1.5 * x[i] * x[j]) * np.cos(1.2 * (x[i] + x[j]))
                
        # Spherical penalty regions with multiple local minima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 15 * (1 - np.exp(-0.08 * (dist_from_origin - 2.5)**2)) * \
                      np.sin(2.2 * np.pi * dist_from_origin)**2
        
        # Add a global scaling factor and combine all components
        return 0.9 * (exp_decay + waves + cross_interactions + penalty)