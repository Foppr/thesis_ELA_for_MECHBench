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
        
        # Enhanced saddle point structure with quadratic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2 * x[i]**2) * np.sin(x[i]) + 0.5 * x[i]**2
        
        # Enhanced cross-term interactions with cubic influence and modified coefficients
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] + x[j]))
        
        # Additional cubic cross-term interaction for increased complexity
        cubic_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_cross += 0.05 * x[i]**3 * x[j]**3 * np.cos(0.2 * (x[i] - x[j]))
        
        return quadratic + chaotic + saddle + cross + cubic_cross