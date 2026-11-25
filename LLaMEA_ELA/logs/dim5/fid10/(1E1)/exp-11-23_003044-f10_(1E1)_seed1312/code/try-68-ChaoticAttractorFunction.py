import numpy as np

class ChaoticAttractorFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Chaotic component using logistic map-like behavior
        for i in range(self.dim):
            # Base quadratic term with varying conditioning
            conditioning = 1.0 + 0.5 * np.sin(i)
            result += conditioning * (x[i] ** 2)
            
            # Add chaotic sinusoidal modulation
            chaotic_term = np.sin(10 * x[i]) * np.cos(7 * x[i])
            result += 0.3 * chaotic_term
            
            # Add interaction terms with other dimensions
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                result += 0.1 * interaction * (1 + 0.1 * i * j)
                
        # Add a global scaling factor based on the norm of the input
        norm_squared = np.sum(x_norm ** 2)
        result *= (1 + 0.2 * norm_squared)
        
        # Add a small random perturbation to make it non-deterministic for different runs
        np.random.seed(int(sum(x) * 1000) % 1000000)
        result += 0.01 * np.random.rand()
        
        return result