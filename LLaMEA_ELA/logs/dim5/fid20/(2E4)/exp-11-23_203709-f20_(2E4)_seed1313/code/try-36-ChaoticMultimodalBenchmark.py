import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic component with highly modified frequencies and polynomial terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += 2.1 * np.sin(5.7 * np.pi * x[i]) * np.cos(6.3 * np.pi * x[i]) + 1.8 * (x[i] ** 4) - 0.9 * (x[i] ** 3)
        
        # Enhanced exponential barrier terms with multiple peaks and varying scales
        barriers = 0
        for i in range(self.dim):
            barriers += 3.2 * np.exp(-0.6 * (x[i] - 2.1)**2) + 2.5 * np.exp(-0.35 * (x[i] + 2.1)**2) + 1.5 * np.exp(-0.5 * (x[i] - 0.5)**2)
        
        # Complex interaction terms with variable coupling and oscillatory behavior
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.05)
                interaction += 1.5 * np.sin(2.3 * r) / (r**3.2 + 0.02) + 0.8 * np.cos(3.1 * r) / (r**2.8 + 0.01)
        
        # Additional chaotic modulation with sine and cosine products
        modulation = 0
        for i in range(self.dim):
            modulation += 0.8 * np.sin(7.2 * x[i]) * np.cos(4.8 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add a global scaling factor and offset
        return 8.3 * chaotic + 3.7 * barriers + 0.15 * interaction + 0.9 * modulation + 35 * self.dim