import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic exponential terms
        for i in range(self.dim):
            xi = x[i]
            # Exponential decay with sinusoidal modulation
            result += np.exp(-0.1 * xi**2) * np.sin(2 * np.pi * xi) * (i + 1)
        
        # Add trigonometric interference terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Pairwise interaction with cosine modulation
                result += 0.5 * np.cos(xi * x[j]) * (i + j + 1)
        
        # Add a global minimum at the origin with quadratic penalty
        result += 0.01 * np.sum(x**2)
        
        # Add a chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(np.pi * x[i]) * np.cos(2 * np.pi * x[i])
        result += 0.3 * chaotic_term
        
        return result