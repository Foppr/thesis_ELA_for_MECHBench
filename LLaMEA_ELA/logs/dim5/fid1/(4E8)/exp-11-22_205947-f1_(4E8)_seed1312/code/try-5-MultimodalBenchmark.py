import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Sinusoidal perturbations to create multiple local minima
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(5.0 * x[i]) * np.cos(2.0 * x[(i + 1) % self.dim])
            
        # Combine terms with different weights
        return polynomial + 0.5 * sinusoidal + 0.1 * np.sum(np.abs(x))