import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute decay factors and frequencies for chaotic behavior
        self.decay_factors = np.exp(-np.arange(dim) * 0.1)
        self.frequencies = 2 * np.pi * (1 + np.arange(dim))
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic component with exponentially decaying correlations
        chaotic = np.sum(self.decay_factors * np.sin(self.frequencies * x_norm) * 
                         np.cos(self.frequencies * x_norm**2))
        
        # Periodic forcing with varying amplitudes
        periodic = np.sum(np.sin(3 * self.frequencies * x_norm) * 
                          np.cos(2 * self.frequencies * x_norm) * 
                          (1 + 0.5 * np.sin(self.frequencies * x_norm)))
        
        # Quadratic basin to guide convergence
        quadratic = np.sum(x_norm**2)
        
        # Add a small noise term to increase ruggedness
        noise = 0.01 * np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        return chaotic + periodic + quadratic + noise