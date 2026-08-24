import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with modified frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(8 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Modified saddle point structure with different polynomial terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**5 - 2.5 * x[i]**3 + 1.5 * x[i]**2) * np.sin(x[i])
        
        # Altered cross-term interactions with different coupling coefficients
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * x[i] * x[j] * np.sin(0.4 * (x[i]**2 + x[j]**2))
        
        # Modified chaotic modulation term
        modulate = 0
        for i in range(self.dim):
            modulate += 0.4 * np.sin(1.5 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.03 * x[i]**2)
        
        return quadratic + chaotic + saddle + cross + modulate