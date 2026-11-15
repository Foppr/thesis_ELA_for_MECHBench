import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Saddle point structure
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2 * x[i]**2) * np.sin(x[i])
        
        # Cross-term interactions
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.1 * x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
        
        return quadratic + chaotic + saddle + cross