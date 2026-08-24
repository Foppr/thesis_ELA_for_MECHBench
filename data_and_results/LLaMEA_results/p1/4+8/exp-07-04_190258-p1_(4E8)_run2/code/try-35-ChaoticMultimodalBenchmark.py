import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with modified frequencies and chaotic scaling
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * x[i]**2) * np.sin(0.5 * x[i]**3)
        
        # Saddle point structure with enhanced non-linearity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 3 * x[i]**4 + 3 * x[i]**2) * np.cos(x[i])
        
        # Enhanced cross-term interactions with cubic and quartic influences
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i] + x[j])) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
        
        # Additional high-frequency chaotic modulation
        high_freq = 0
        for i in range(self.dim):
            high_freq += 0.5 * np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(2 * x[i]**2)
        
        return quadratic + chaotic + saddle + cross + high_freq