import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with higher frequency
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced saddle point structure with higher-order terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 3 * x[i]**4 + 2 * x[i]**2) * np.sin(x[i])
        
        # Enhanced cross-term interactions with nonlinear coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * np.sin(0.3 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic modulation term
        modulate = 0
        for i in range(self.dim):
            modulate += 0.5 * np.sin(2 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        return quadratic + chaotic + saddle + cross + modulate