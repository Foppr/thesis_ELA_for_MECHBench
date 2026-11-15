import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Exponential barrier terms to create rugged landscape
        f2 = np.sum(np.exp(-5.0 * np.abs(x_norm)))
        
        # Sinusoidal modulation with varying frequencies
        f3 = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic += 4 * 0.5 * (1 - 0.5)
            else:
                chaotic += 4 * x_norm[i-1] * (1 - x_norm[i-1])
        f4 = chaotic
        
        # Combine all terms with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.4 * f3 + 0.1 * f4