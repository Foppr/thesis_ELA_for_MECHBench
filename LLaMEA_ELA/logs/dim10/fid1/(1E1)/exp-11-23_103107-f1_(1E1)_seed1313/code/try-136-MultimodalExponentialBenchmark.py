import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with dynamic phase shifts and varying decay rates
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.3 * np.sum(x))**3)
        
        # Nested trigonometric wave interactions with fractal-like frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                     np.cos(9 * x[i]) * np.sin(4 * x[i]) + 
                     np.sin(3 * x[i]) * np.cos(11 * x[i]) + 
                     np.cos(6 * x[i]) * np.sin(8 * x[i])) * \
                     (1 + 0.2 * np.sin(2 * np.pi * i / self.dim))
            
        # Chaotic cross-dimensional interactions with fractal coupling and time-varying coefficients
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.sin(0.3 * (i + j)) * np.cos(0.4 * (i - j))
                cross_interactions += coupling_strength * \
                                   np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j] * 0.5) * \
                                   np.cos(x[i] + x[j] * 0.7) * \
                                   (1 + 0.3 * np.sin(0.6 * (x[i] - x[j])**3))
                
        # Adaptive penalty regions with nested local minima and dynamic scaling
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.08 * (dist_from_origin - 4)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.15 * (dist_from_origin - 2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.exp(-0.1 * (dist_from_origin - 1.5)**2) * \
                      np.sin(6 * np.pi * dist_from_origin)**2
        
        # Add global scaling factor and combine all components with enhanced non-linearity
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)