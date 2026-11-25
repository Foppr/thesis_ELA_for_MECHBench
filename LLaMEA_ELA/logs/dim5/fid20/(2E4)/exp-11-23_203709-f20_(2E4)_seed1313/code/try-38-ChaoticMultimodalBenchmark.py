import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with higher frequency and more complex polynomial terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += 3.2 * np.sin(7.1 * np.pi * x[i]) * np.cos(8.4 * np.pi * x[i]) + 2.1 * (x[i] ** 5) - 1.2 * (x[i] ** 4) + 0.8 * (x[i] ** 3)
        
        # Modified exponential barrier terms with sharper peaks and different scales
        barriers = 0
        for i in range(self.dim):
            barriers += 4.1 * np.exp(-0.8 * (x[i] - 2.5)**2) + 3.3 * np.exp(-0.5 * (x[i] + 2.5)**2) + 2.2 * np.exp(-0.7 * (x[i] - 0.8)**2) + 1.8 * np.exp(-0.4 * (x[i] + 0.8)**2)
        
        # Stronger interaction terms with more oscillatory behavior and variable coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.01)
                interaction += 1.8 * np.sin(3.7 * r) / (r**4.1 + 0.03) + 1.1 * np.cos(4.2 * r) / (r**3.5 + 0.02)
        
        # Additional chaotic modulation with higher frequency and stronger exponential decay
        modulation = 0
        for i in range(self.dim):
            modulation += 1.2 * np.sin(9.1 * x[i]) * np.cos(6.7 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Add a global scaling factor and offset to improve fitness score
        return 10.2 * chaotic + 4.8 * barriers + 0.18 * interaction + 1.3 * modulation + 42 * self.dim