import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with dynamic phase shifts and variable decay rates
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x + 0.3 * np.sum(x))**3)
        
        # Nested trigonometric waves with fractal-like frequency modulation
        waves = 0
        for i in range(self.dim):
            waves += np.sin(7 * x[i]) * np.cos(9 * x[i]) * np.sin(2 * x[i]**2) + \
                    np.cos(11 * x[i]) * np.sin(5 * x[i]) * np.cos(3 * x[i]**2) + \
                    np.sin(4 * x[i]) * np.cos(8 * x[i]) * np.sin(x[i] * np.cos(x[i]))
            
        # Dynamic cross-dimensional interactions with adaptive coupling strength and chaotic modulation
        cross_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on solution density
                coupling_factor = 1 + 0.3 * np.sin(2 * np.pi * (x[i] + x[j]))
                cross_interactions += coupling_factor * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                                   np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                                   np.tan(0.3 * (x[i] - x[j])**2)
                
        # Dynamic penalty regions with nested local minima and solution density adaptation
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            # Density-adaptive penalties
            density_factor = 1 + 0.5 * np.sin(3 * dist_from_origin)
            penalty += density_factor * 20 * (1 - np.exp(-0.08 * (dist_from_origin - 4)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      8 * np.exp(-0.12 * (dist_from_origin - 2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3
        
        # Add a global scaling factor and combine all components
        return 1.1 * (exp_decay + waves + cross_interactions + penalty)