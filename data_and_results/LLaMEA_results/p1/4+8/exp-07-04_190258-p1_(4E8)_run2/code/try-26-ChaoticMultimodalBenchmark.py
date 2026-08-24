import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal modulation with higher frequency
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced saddle point perturbation with cubic terms
        saddle = 0
        for i in range(self.dim):
            saddle += 0.3 * x[i]**3 * np.sin(1.5 * x[i]) * np.cos(0.3 * x[i])
        
        # Enhanced cross-term interaction with higher-order coupling
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += x[i] * x[i+1] * np.sin(2 * (x[i] + x[i+1])) * np.cos(0.5 * (x[i] - x[i+1]))
        
        # Additional chaotic coupling between all dimensions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.1 * x[i] * x[j] * np.sin(3 * (x[i]**2 + x[j]**2))
        
        return quadratic + chaotic + saddle + cross_term + coupling