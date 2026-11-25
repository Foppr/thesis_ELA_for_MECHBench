import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with dynamic scaling and phase modulation
        exp_terms = 0
        for i in range(self.dim):
            exp_terms += np.exp(-0.2 * (x[i]**2)) * np.sin(5 * x[i] + 0.3 * np.sum(x**2))**3
        
        # Nested trigonometric waves with varying amplitudes and frequencies
        wave_terms = 0
        for i in range(self.dim):
            wave_terms += (np.sin(7 * x[i]) * np.cos(4 * x[i]) + 
                          np.cos(9 * x[i]) * np.sin(2 * x[i]) + 
                          np.sin(6 * x[i]) * np.cos(3 * x[i]) + 
                          np.cos(5 * x[i]) * np.sin(8 * x[i]))
            
        # Dynamic cross-dimensional interactions with adaptive coupling strength
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                coupling = 1 + 0.3 * np.sin(2 * np.pi * dist) * np.cos(3 * np.pi * dist)
                cross_terms += coupling * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                              np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Dynamic penalty regions with fractal-like structure and multiple local minima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 2)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.1 * (dist_from_origin - 4)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.sin(6 * np.pi * dist_from_origin)**2
        
        # Add global scaling and combine all components with enhanced nonlinearity
        return 1.2 * (exp_terms + wave_terms + cross_terms + penalty) + \
               0.5 * np.sum(np.sin(10 * x)) * np.cos(0.5 * np.sum(x**2))