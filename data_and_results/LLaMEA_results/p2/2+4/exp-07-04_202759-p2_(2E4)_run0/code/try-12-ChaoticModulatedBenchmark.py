import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using logistic map-like behavior with cross-terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.exp(-0.1 * np.abs(x[i])) * np.sin(3 * np.pi * x[i])
            # Add interaction term between adjacent dimensions
            if i > 0:
                chaotic += 0.05 * np.sin(x[i-1] + x[i]) * np.cos(0.5 * x[i])
        
        # Exponential decay component with modified frequency
        decay = 0
        for i in range(self.dim):
            decay += np.exp(-0.05 * x[i]**2) * np.cos(2.5 * x[i])
        
        # Sinusoidal modulation with increased frequency and interaction
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            # Add cross-dimensional interaction
            if i > 0:
                modulation += 0.03 * np.sin(x[i-1] * x[i]) * np.cos(0.3 * x[i-1])
        
        # Combine all components with different weights
        return 0.6 * chaotic + 0.25 * decay + 0.2 * modulation + 0.1 * np.sum(x**4)