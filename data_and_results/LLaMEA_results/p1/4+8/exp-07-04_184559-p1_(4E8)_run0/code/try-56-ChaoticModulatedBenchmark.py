import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal modulation with higher frequency
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.exp(-0.3 * np.sum(x_norm**2)))
        
        # Modified exponential barrier with sharper transition
        barriers = np.exp(-0.2 * np.sum(np.abs(x_norm)**4))
        
        # Chaotic component with additional interaction terms
        chaotic = np.sum(np.sin(2.5 * np.pi * x_norm) * np.cos(3.5 * np.pi * x_norm) * np.sin(np.pi * x_norm))
        
        # Combine all components with adjusted weights
        return f1 + 1.5 * f2 + 0.7 * barriers + 0.4 * chaotic