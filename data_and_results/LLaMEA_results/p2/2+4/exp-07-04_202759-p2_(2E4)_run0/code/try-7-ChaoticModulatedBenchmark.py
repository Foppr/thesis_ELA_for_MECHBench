import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.exp(-0.1 * np.abs(x[i])) * np.sin(3 * np.pi * x[i])
        
        # Exponential decay component
        decay = 0
        for i in range(self.dim):
            decay += np.exp(-0.05 * x[i]**2) * np.cos(2 * x[i])
        
        # Sinusoidal modulation
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
        
        # Combine all components with different weights
        return 0.7 * chaotic + 0.3 * decay + 0.2 * modulation + 0.1 * np.sum(x**4)