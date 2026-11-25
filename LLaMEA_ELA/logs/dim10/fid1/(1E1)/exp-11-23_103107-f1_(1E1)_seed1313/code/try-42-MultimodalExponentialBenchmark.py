import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with fractional powers and dynamic phase shifts
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x)**1.7) * np.sin(2.5 * np.pi * x + 0.3 * np.sum(x))**3)
        
        # Augmented trigonometric wave interactions with non-linear coupling and harmonic mixing
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i])**2 + np.cos(7 * x[i])**2) * \
                    (np.sin(3 * x[i]) * np.cos(4 * x[i]) + 
                     np.cos(6 * x[i]) * np.sin(2 * x[i])) + \
                    np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.sin(x[i]**2)
            
        # Complex cross-dimensional interactions with fractional exponents and chaotic coupling
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (np.abs(x[i])**1.5 + np.abs(x[j])**1.5)) * \
                                   np.sin(x[i] * x[j] * 0.7) * np.cos(x[i] + x[j] * 0.3) * \
                                   (1 + 0.3 * np.sin(0.8 * (x[i] - x[j])**2.5) * 
                                    np.cos(0.6 * (x[i] + x[j])**1.8))
                
        # Complex penalty regions with nested minima, irregular scaling, and chaotic behavior
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 2.5)**2.2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      8 * np.exp(-0.15 * (dist_from_origin - 1.2)**2.5) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      12 * np.exp(-0.08 * (dist_from_origin - 4.0)**2.1) * \
                      np.sin(2 * np.pi * dist_from_origin)**4
        
        # Add global scaling factor and combine all components with chaotic mixing
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)