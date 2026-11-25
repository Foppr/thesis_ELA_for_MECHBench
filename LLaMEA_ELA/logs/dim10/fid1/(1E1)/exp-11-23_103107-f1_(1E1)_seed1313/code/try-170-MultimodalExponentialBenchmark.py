import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Enhanced chaotic exponential terms with dynamic phase shifts and varying decay rates
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.7 * np.sin(2 * x))**3)
        
        # Complex trigonometric wave interactions with non-linear coupling and frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                     np.cos(9 * x[i]) * np.sin(4 * x[i]) + 
                     np.sin(3 * x[i]) * np.cos(8 * x[i]) +
                     np.cos(6 * x[i]) * np.sin(2 * x[i])) * \
                     (1 + 0.3 * np.sin(0.5 * x[i]**2))
            
        # Stronger chaotic cross-dimensional interactions with fractal-like coupling and time-delay effects
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interactions += np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j] + 0.5 * np.sin(x[i])) * \
                                   np.cos(x[i] + x[j] + 0.3 * np.cos(x[j])) * \
                                   (1 + 0.4 * np.sin(0.7 * (x[i] - x[j])**3))
                
        # Complex multi-scale penalty regions with fractal-like structure and chaotic minima distribution
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.08 * (dist_from_origin - 4)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin + 0.5 * np.sin(3 * dist_from_origin))**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin + 0.3 * np.cos(2 * dist_from_origin))**4
        
        # Add global scaling factor and combine all components with chaotic mixing
        return 1.2 * (exp_decay + waves + cross_interactions + penalty) + \
               0.5 * np.sin(10 * np.sum(x**2)) * np.cos(8 * np.sum(x**3))