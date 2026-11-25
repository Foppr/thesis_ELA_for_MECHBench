import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using sine and cosine functions
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(7 * x[i])
        
        # Polynomial potential component
        polynomial = 0
        for i in range(self.dim):
            polynomial += x[i]**6 - 15 * x[i]**4 + 75 * x[i]**2 - 125
        
        # Cross-dimensional interaction term with exponential decay
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 0.01)
                interaction += np.exp(-distance) * np.sin(2 * np.pi * (x[i] + x[j]))
        
        # Add a global scaling factor and offset
        return 0.1 * chaotic + 0.01 * polynomial + 0.3 * interaction + 5 * self.dim