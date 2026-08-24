import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with exponential decay and frequency modulation
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * x[i]**2) * np.sin(0.5 * x[i]**3)
        
        # Enhanced saddle point structure with quartic and quintic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 3 * x[i]**2 + 0.5 * x[i]**5) * np.sin(x[i])
        
        # Complex cross-term interactions with cubic and quintic influences
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic noise term to increase landscape irregularity
        noise = 0
        for i in range(self.dim):
            noise += 0.05 * np.sin(13 * x[i]) * np.cos(7 * x[i]) * np.tan(0.1 * x[i])
        
        return quadratic + chaotic + saddle + cross + noise