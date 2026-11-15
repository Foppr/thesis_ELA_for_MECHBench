import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with hyperbolic tangent chaos and adaptive frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.tanh(5 * x[i]) * np.sin(3 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Saddle point structure with enhanced nonlinearity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 3 * x[i]**2) * np.tanh(x[i])
        
        # Enhanced cross-term interactions with adaptive cubic and quartic coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] + x[j])) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
        
        # Additional hyperbolic coupling term for increased conditioning
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += 0.1 * np.sinh(0.5 * x[i]) * np.cos(2 * x[i])
        
        return quadratic + chaotic + saddle + cross + hyperbolic