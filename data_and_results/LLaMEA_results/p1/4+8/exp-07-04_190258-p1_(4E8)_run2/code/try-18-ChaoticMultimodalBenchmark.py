import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal modulation
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Saddle point perturbation
        saddle = 0
        for i in range(self.dim):
            saddle += 0.5 * x[i] * np.sin(2 * x[i]) * np.cos(0.5 * x[i])
        
        # Cross-term interaction
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += x[i] * x[i+1] * np.sin(x[i] + x[i+1])
        
        return quadratic + chaotic + saddle + cross_term