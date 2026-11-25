import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic component with modified frequencies and cubic terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += 1.2 * np.sin(3.5 * np.pi * x[i]) * np.cos(4.2 * np.pi * x[i]) + 0.7 * (x[i] ** 3)
        
        # Enhanced exponential barrier terms with different shifts and scaling
        barriers = 0
        for i in range(self.dim):
            barriers += 2.0 * np.exp(-0.4 * (x[i] - 1.8)**2) + 1.2 * np.exp(-0.25 * (x[i] + 1.8)**2)
        
        # Modified interaction terms with altered coupling strength
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.03)
                interaction += 0.8 * np.sin(r) / (r**2.5 + 0.01)
        
        # Add a global scaling factor and offset
        return 6.5 * chaotic + 2.5 * barriers + 0.07 * interaction + 22 * self.dim