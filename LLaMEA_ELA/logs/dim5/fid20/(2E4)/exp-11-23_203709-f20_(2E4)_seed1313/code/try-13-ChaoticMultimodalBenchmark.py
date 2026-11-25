import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic component using sine and cosine
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Exponential barrier terms to create rugged terrain
        barriers = 0
        for i in range(self.dim):
            barriers += np.exp(-0.5 * (x[i] - 2)**2) + np.exp(-0.5 * (x[i] + 2)**2)
        
        # Interaction terms with quadratic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.1)
                interaction += np.sin(r) / (r + 0.1)
        
        # Add a global scaling factor and offset
        return 5 * chaotic + 2 * barriers + 0.1 * interaction + 15 * self.dim