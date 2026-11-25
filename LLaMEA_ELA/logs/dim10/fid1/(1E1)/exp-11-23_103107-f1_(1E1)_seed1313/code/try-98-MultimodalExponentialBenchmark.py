import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential terms with fractional powers and dynamic phase shifts
        exp_terms = 0
        for i in range(self.dim):
            exp_terms += np.exp(-0.2 * np.abs(x[i])**1.7) * np.sin(5 * np.pi * x[i] + 0.3 * i)**3
        
        # Highly coupled trigonometric waves with chaotic frequency modulation
        wave_terms = 0
        for i in range(self.dim):
            wave_terms += (np.sin(7 * x[i]) * np.cos(9 * x[i]) + 
                          np.cos(5 * x[i]) * np.sin(11 * x[i]) + 
                          np.sin(3 * x[i]) * np.cos(13 * x[i]) +
                          np.cos(2 * x[i]) * np.sin(17 * x[i]))
            
        # Complex cross-dimensional interactions with fractal-like coupling
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited but strong coupling
                cross_terms += np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                              np.sin(x[i] * x[j] * 0.5) * \
                              np.cos(x[i] + x[j]) * \
                              (1 + 0.3 * np.sin(0.7 * (x[i] - x[j])**3))
                
        # Nested penalty regions with multiple scales and chaotic minima
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 2.5)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      10 * np.exp(-0.12 * (dist_from_origin - 1.2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      8 * (1 - np.exp(-0.08 * (dist_from_origin - 4.0)**2)) * \
                      np.sin(2 * np.pi * dist_from_origin)**4
        
        # Add global scaling and combine all components with chaotic weighting
        return 1.2 * (exp_terms + wave_terms + cross_terms + penalty) + \
               0.5 * np.sin(0.5 * np.sum(x**3)) * np.cos(0.3 * np.sum(x**4))