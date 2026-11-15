import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal modulation with chaotic behavior
        f2 = np.sum(np.sin(np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Exponential barrier terms to create complex landscape
        barriers = np.exp(-0.1 * np.sum(np.abs(x_norm)**3))
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Combine all components
        return f1 + 2.0 * f2 + 0.5 * barriers + 0.3 * chaotic