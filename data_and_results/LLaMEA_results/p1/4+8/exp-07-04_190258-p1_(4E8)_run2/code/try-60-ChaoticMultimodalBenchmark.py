import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with modified frequencies and hyperbolic terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.03 * x[i]**2) + 
                       0.5 * np.tanh(2 * x[i]) * np.log(1 + np.abs(x[i])))
        
        # Saddle point structure with higher-order polynomials
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 3 * x[i]**4 + 3 * x[i]**2) * np.sin(x[i])
        
        # Enhanced cross-term interactions with cubic influence and additional logarithmic coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] + x[j])) * np.log(1 + np.abs(x[i] * x[j]))
        
        # Additional chaotic cross-terms with exponential decay
        chaotic_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_cross += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        return quadratic + chaotic + saddle + cross + chaotic_cross