import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic component with higher frequencies and cubic terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(3 * np.pi * x[i]) * np.cos(4 * np.pi * x[i]) + 0.5 * (x[i] ** 3)
        
        # Enhanced exponential barrier terms with different shifts
        barriers = 0
        for i in range(self.dim):
            barriers += 1.5 * np.exp(-0.3 * (x[i] - 1.5)**2) + 1.5 * np.exp(-0.3 * (x[i] + 1.5)**2)
        
        # Modified interaction terms with inverse cubic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.05)
                interaction += np.sin(r) / (r**3 + 0.01)
        
        # Add a global scaling factor and offset
        return 7 * chaotic + 3 * barriers + 0.05 * interaction + 20 * self.dim