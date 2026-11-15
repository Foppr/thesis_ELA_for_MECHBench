import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using sine and exponential decay
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Correlated variables with exponential decay
        correlated = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correlated += np.exp(-0.05 * (x[i] - x[j])**2) * np.sin(x[i] * x[j])
                
        # Sinusoidal modulation with varying frequencies
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(2 * np.pi * x[i] * (i + 1)) * np.cos(0.5 * np.pi * x[i])
            
        # Combine components with different weights
        return 0.5 * np.sum(x**2) + 0.3 * chaotic + 0.2 * correlated + 0.1 * modulation