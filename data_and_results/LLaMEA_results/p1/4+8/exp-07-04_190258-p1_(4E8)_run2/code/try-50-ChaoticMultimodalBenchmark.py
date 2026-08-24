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
            chaotic += np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Enhanced saddle point structure with higher-order terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 3 * x[i]**4 + 3 * x[i]**2) * np.sin(x[i])
        
        # Enhanced cross-term interactions with cubic influence and additional coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
        
        # Additional chaotic modulation term for increased complexity
        modulate = 0
        for i in range(self.dim):
            modulate += 0.1 * np.sin(11 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        return quadratic + chaotic + saddle + cross + modulate