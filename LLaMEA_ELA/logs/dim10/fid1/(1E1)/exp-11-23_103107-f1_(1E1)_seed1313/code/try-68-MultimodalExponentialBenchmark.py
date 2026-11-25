import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential components with non-linear parameter modulation
        exp_terms = 0
        for i in range(self.dim):
            exp_terms += np.exp(-0.5 * (x[i]**2)) * np.sin(5 * np.pi * x[i] + 0.3 * i)**3
        
        # Nested trigonometric patterns with varying coupling strengths and phase shifts
        nested_waves = 0
        for i in range(self.dim):
            nested_waves += (np.sin(7 * x[i]) * np.cos(11 * x[i]) + 
                           np.cos(9 * x[i]) * np.sin(13 * x[i]) + 
                           np.sin(5 * x[i]) * np.cos(17 * x[i]) +
                           np.cos(3 * x[i]) * np.sin(19 * x[i]))
            
        # Stronger cross-dimensional coupling with chaotic interaction terms
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j] * 0.5) * \
                                   np.cos(x[i] + x[j] * 0.7) * \
                                   np.tan(0.2 * (x[i] - x[j])**2) * \
                                   (1 + 0.3 * np.sin(0.3 * (x[i] + x[j])**3))
                
        # Adaptive penalty regions with fractal-like structure and multiple attraction points
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.1 * (dist_from_origin - 2.5)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 1.5)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.exp(-0.08 * (dist_from_origin - 4.0)**2) * \
                      np.sin(6 * np.pi * dist_from_origin)**2
        
        # Add chaotic scaling factor and combine all components
        return 1.2 * (exp_terms + nested_waves + cross_interactions + penalty)