import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with varying decay rates and phase shifts
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.3)**3)
        
        # Nested trigonometric wave interactions with multiple frequencies and coupling
        waves = 0
        for i in range(self.dim):
            waves += (np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                     np.cos(9 * x[i]) * np.sin(4 * x[i]) + 
                     np.sin(3 * x[i]) * np.cos(10 * x[i]) + 
                     np.cos(6 * x[i]) * np.sin(8 * x[i]))
            
        # Chaotic cross-dimensional interactions with fractal-like coupling and time-varying coefficients
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = np.sin(0.3 * (x[i] - x[j])**2) + 0.5
                cross_interactions += np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                                   coupling_factor * \
                                   (1 + 0.3 * np.sin(0.7 * (x[i] - x[j])**3))
                
        # Adaptive penalty regions with nested local minima and dynamic scaling
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 2.5)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      8 * np.exp(-0.12 * (dist_from_origin - 1.5)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      12 * (1 - np.exp(-0.08 * (dist_from_origin - 4)**2)) * \
                      np.sin(2 * np.pi * dist_from_origin)**4
        
        # Add a global scaling factor and combine all components
        return 1.2 * (exp_decay + waves + cross_interactions + penalty)