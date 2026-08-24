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
            chaotic += np.exp(-0.5 * (x[i] - np.sin(x[i]))**2) * np.cos(3 * x[i])
        
        # Sinusoidal modulation with varying frequencies
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(2 * np.pi * x[i] / (1 + np.abs(x[i]))) * np.cos(0.5 * x[i])
        
        # Exponential decay component
        decay = 0
        for i in range(self.dim):
            decay += np.exp(-0.1 * np.abs(x[i])) * np.sin(0.3 * x[i])
        
        # Interaction terms with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                interaction += 0.05 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2 * (x[i] + x[j]))
        
        # Global minimum at origin with additional penalty
        penalty = 0.1 * np.sum(x**4)
        
        return chaotic + modulation + decay + interaction + penalty