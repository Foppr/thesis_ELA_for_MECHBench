import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential barrier terms to create complex boundaries
        barrier = np.sum(np.exp(1.0 / (1.0 - np.sum(x_norm**2))) * (np.sum(x_norm**2) < 1.0))
        
        # Sinusoidal modulation with chaotic behavior
        modulated = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Cross-dimensional interaction creating ruggedness
        rugged = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                       np.exp(-0.5 * np.sum((x_norm[:-1] - x_norm[1:])**2)))
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.sum(np.sin(np.pi * np.abs(x_norm)) * np.exp(-np.sum(np.abs(x_norm))))
        
        # Combine all components
        return 1.5 * barrier + 2.0 * modulated + 1.0 * rugged + 0.8 * chaotic