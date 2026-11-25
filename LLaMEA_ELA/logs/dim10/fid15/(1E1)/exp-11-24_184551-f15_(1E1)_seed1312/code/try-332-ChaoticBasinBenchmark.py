import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Base polynomial basin term
        basin = 0.1 * np.sum(x**4)
        
        # Chaotic sinusoidal modulations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i])
            
        # Add exponential barriers at boundaries
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-((x[i] - 5.0)**2)) + np.exp(-((x[i] + 5.0)**2))
            
        # Add a complex interaction term between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x[i] * x[j]) / (1.0 + (x[i] - x[j])**2)
                
        # Add a global scaling factor
        scale = 1.0 + 0.5 * np.sin(np.sum(x**2) / 10.0)
        
        return scale * (basin + chaotic - interaction) + barrier