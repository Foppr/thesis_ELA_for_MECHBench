import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave components with varying frequencies
        sin_term = np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        # Polynomial potential terms with mixed degrees
        poly_term = np.sum(x**6 - 15 * x**4 + 75 * x**2 - 125)
        
        # Logarithmic barrier terms to enforce boundaries
        log_barrier = np.sum(-np.log(25.0 - x**2))
        
        # Chaotic component using a modified logistic map
        chaotic = 0.0
        for i in range(min(5, self.dim)):
            if i < len(x):
                chaotic += np.sin(100 * np.sin(x[i])) * np.cos(50 * np.sin(x[i]))
        
        # Combine all terms with different weights
        return 0.2 * sin_term + 0.1 * poly_term + 0.05 * log_barrier + 0.01 * chaotic + 1.5