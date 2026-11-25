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
            chaotic += 2.5 * np.sin(6.1 * np.pi * x[i]) * np.cos(7.2 * np.pi * x[i]) + 2.1 * (x[i] ** 4) - 1.1 * (x[i] ** 3)
        
        # Enhanced exponential barrier terms with multiple peaks and varying scales
        barriers = 0
        for i in range(self.dim):
            barriers += 3.5 * np.exp(-0.7 * (x[i] - 2.3)**2) + 2.8 * np.exp(-0.4 * (x[i] + 2.3)**2) + 1.8 * np.exp(-0.6 * (x[i] - 0.7)**2)
        
        # Complex interaction terms with variable coupling and oscillatory behavior
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.03)
                interaction += 1.5 * np.sin(2.7 * r) / (r**3.5 + 0.01) + 0.8 * np.cos(3.5 * r) / (r**3.0 + 0.005)
        
        # Additional chaotic modulation with sine and cosine products
        modulation = 0
        for i in range(self.dim):
            modulation += 1.0 * np.sin(8.1 * x[i]) * np.cos(5.3 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Add a global scaling factor and offset
        return 9.1 * chaotic + 4.2 * barriers + 0.15 * interaction + 1.1 * modulation + 40 * self.dim