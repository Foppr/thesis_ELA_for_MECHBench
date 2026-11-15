import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with modified frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.03 * x[i]**2)
        
        # Enhanced saddle point structure with cubic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 3 * x[i]**2 + 0.5 * x[i]**3) * np.sin(x[i])
        
        # Enhanced cross-term interactions with cubic cross-terms
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.15 * x[i] * x[j] * (x[i] + x[j]) * np.sin(0.6 * (x[i] + x[j]))
        
        return quadratic + chaotic + saddle + cross