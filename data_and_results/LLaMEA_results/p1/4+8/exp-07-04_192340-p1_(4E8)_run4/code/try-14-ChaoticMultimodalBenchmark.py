import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.exp(-0.5 * (x[i] - np.sin(x[i]))**2) * np.cos(2 * np.pi * x[i])
            
        # Exponential decay terms
        decay = 0
        for i in range(self.dim):
            decay += np.exp(-0.1 * np.abs(x[i])) * np.sin(0.5 * x[i])**2
            
        # Sinusoidal modulation with varying frequencies
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Interaction terms with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        return chaotic + decay + modulation + interaction