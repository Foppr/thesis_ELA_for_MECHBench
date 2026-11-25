import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Enhanced exponential decay with varying amplitudes
        exp_decay = np.sum(np.exp(-0.3 * x**2) * (np.sin(3 * x)**2 + 0.5 * np.cos(2 * x)**2))
        
        # Improved trigonometric wave interactions with frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(4 * x[i]) * np.cos(6 * x[i]) + 
                     np.cos(8 * x[i]) * np.sin(3 * x[i])) * (1 + 0.3 * np.sin(0.5 * x[i]))
            
        # Enhanced cross-dimensional interactions with coupled exponential and trigonometric terms
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.2 * (x[i]**2 + x[j]**2)) * \
                                   (np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) + 
                                    0.5 * np.sin(x[i] + x[j])**2)
                
        # Modified spherical penalty with multiple attraction points
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 15 * (1 - np.exp(-0.15 * (dist_from_origin - 2.5)**2)) * \
                      (np.sin(3 * dist_from_origin)**2 + 0.3 * np.cos(2 * dist_from_origin)**2)
        
        # Add a global scaling factor and combine all components
        return 0.9 * (exp_decay + waves + cross_interactions + penalty)