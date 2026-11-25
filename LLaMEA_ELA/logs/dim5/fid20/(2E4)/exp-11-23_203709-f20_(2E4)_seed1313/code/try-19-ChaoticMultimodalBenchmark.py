import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) + 
                       0.5 * np.sin(5 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]))
        
        # Enhanced exponential barrier terms with multiple peaks
        barriers = 0
        for i in range(self.dim):
            barriers += (np.exp(-0.3 * (x[i] - 2.5)**2) + 
                        np.exp(-0.3 * (x[i] + 2.5)**2) + 
                        0.7 * np.exp(-0.4 * (x[i] - 1.0)**2) + 
                        0.7 * np.exp(-0.4 * (x[i] + 1.0)**2))
        
        # Enhanced interaction terms with adaptive coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.05)
                interaction += (np.sin(r) / (r + 0.05) + 
                               0.3 * np.cos(2 * r) / (r + 0.05))
        
        # Add a global scaling factor and offset
        return 3 * chaotic + 1.5 * barriers + 0.2 * interaction + 20 * self.dim