import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Exponential growth component
        exp_term = 0
        for i in range(self.dim):
            exp_term += np.exp(0.1 * x[i]**2) - 1
        
        # Sinusoidal perturbations with varying frequencies
        sin_term = 0
        for i in range(self.dim):
            sin_term += np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.5 * np.sin(7 * x[i])
        
        # Chaotic cross-dimensional interaction
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += np.sin(x[i] * x[j]) * np.exp(-0.01 * (x[i] - x[j])**2)
        
        # Add a global scaling factor to increase complexity
        return f_val + 0.3 * exp_term + 0.2 * sin_term + 0.1 * chaotic_term