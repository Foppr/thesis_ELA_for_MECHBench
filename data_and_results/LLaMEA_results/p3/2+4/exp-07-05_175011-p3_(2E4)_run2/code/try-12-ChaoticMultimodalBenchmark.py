import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Modified decay factors and frequencies for increased complexity
        self.decay_factors = np.exp(-np.arange(dim) * 0.15)
        self.frequencies = 2 * np.pi * (1.5 + np.arange(dim) * 0.5)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced chaotic component with coupled interactions
        chaotic = np.sum(self.decay_factors * np.sin(self.frequencies * x_norm) * 
                         np.cos(self.frequencies * x_norm**1.5))
        
        # Modified periodic forcing with higher harmonic coupling
        periodic = np.sum(np.sin(4 * self.frequencies * x_norm) * 
                          np.cos(3 * self.frequencies * x_norm) * 
                          (1 + 0.3 * np.sin(2 * self.frequencies * x_norm)))
        
        # Quadratic basin with slight asymmetry
        quadratic = np.sum(x_norm**2 * (1 + 0.1 * np.sin(x_norm)))
        
        # Increased noise term with more complex structure
        noise = 0.02 * np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * np.sin(5 * x_norm))
        
        return chaotic + periodic + quadratic + noise