import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies and hyperbolic terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.tanh(0.1 * x[i]) + 
                       np.log(1 + np.abs(x[i])) * np.exp(-0.05 * x[i]**2))
        
        # Higher-order saddle point structure with cubic and quartic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 3 * x[i]**4 + 3 * x[i]**2) * np.sin(x[i]) + \
                     0.5 * x[i]**3 * np.cos(2 * x[i])
        
        # Intricate cross-term interactions with hyperbolic and logarithmic coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (0.2 * x[i] * x[j] * (x[i]**2 + x[j]**2) * 
                         np.sin(0.5 * (x[i] + x[j])) * 
                         np.cosh(0.05 * (x[i] - x[j])) * 
                         np.log(2 + np.abs(x[i] * x[j])))
        
        # Additional cubic cross-term with exponential coupling
        cubic_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    cubic_cross += 0.05 * x[i] * x[j] * x[k] * np.sin(0.2 * (x[i] + x[j] + x[k]))
        
        return quadratic + chaotic + saddle + cross + cubic_cross