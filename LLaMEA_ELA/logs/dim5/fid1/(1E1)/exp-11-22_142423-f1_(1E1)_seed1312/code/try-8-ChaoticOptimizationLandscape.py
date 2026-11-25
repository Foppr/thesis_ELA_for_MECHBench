import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base term: quadratic with exponential penalty
        f = np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Chaotic oscillation terms
        for i in range(self.dim):
            f += 0.5 * np.sin(3 * x[i]) * np.cos(5 * x[(i + 1) % self.dim]) * np.exp(-0.05 * x[i]**2)
            
        # Saddle-point structure with interaction terms
        for i in range(self.dim):
            f += 0.3 * (x[i]**2 - 1)**2 * np.sin(2 * x[(i + 2) % self.dim])
            
        # Additional chaotic component using logistic map-like behavior
        logistic_term = 0.2 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)))
        
        f += logistic_term
        
        # Penalty for large values to maintain bounded search space
        f += 0.01 * np.sum(np.abs(x)**3)
        
        return f