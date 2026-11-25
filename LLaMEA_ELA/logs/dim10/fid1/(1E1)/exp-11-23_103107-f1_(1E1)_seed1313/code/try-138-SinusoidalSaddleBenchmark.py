import numpy as np

class SinusoidalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Periodic sinusoidal components with varying amplitudes and frequencies
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                           (1 + 0.5 * np.sin(np.pi * x**2)))
        
        # Asymmetric saddle points with different curvature in each dimension
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**4 - 2 * x[i]**2) * np.cos(0.5 * np.pi * x[i]) + \
                      0.5 * x[i]**3 * np.sin(2 * np.pi * x[i])
            
        # Layered penalty regions with varying intensity and shape
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.abs(x[i])
            penalty += 10 * (dist_from_origin - 2)**2 * np.exp(-0.1 * (dist_from_origin - 2)**2) + \
                      5 * np.sin(0.3 * dist_from_origin)**2 * np.cos(0.7 * dist_from_origin)
            
        # Cross-dimensional interaction terms with asymmetric coupling
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j]) * \
                              np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Global scaling and combination of components
        return 0.8 * (sinusoidal + saddles + penalty + cross_terms) + 1.5 * np.sum(x**4)