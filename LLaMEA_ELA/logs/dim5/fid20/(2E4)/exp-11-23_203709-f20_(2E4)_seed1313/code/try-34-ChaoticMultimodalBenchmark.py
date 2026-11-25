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
            chaotic += 1.5 * np.sin(4.0 * np.pi * x[i]) * np.cos(5.0 * np.pi * x[i]) + 0.9 * (x[i] ** 3) + 0.3 * np.sin(7.0 * np.pi * x[i])
        
        # Enhanced exponential barrier terms with different shifts and scaling
        barriers = 0
        for i in range(self.dim):
            barriers += 2.5 * np.exp(-0.5 * (x[i] - 2.0)**2) + 1.5 * np.exp(-0.3 * (x[i] + 2.0)**2) + 0.8 * np.exp(-0.1 * x[i]**2)
        
        # Modified interaction terms with altered coupling strength and additional harmonic components
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.05)
                interaction += 1.0 * np.sin(r) / (r**3 + 0.01) + 0.5 * np.cos(2*r) / (r**1.5 + 0.02)
        
        # Add a global scaling factor and offset
        return 8.0 * chaotic + 3.0 * barriers + 0.1 * interaction + 25 * self.dim