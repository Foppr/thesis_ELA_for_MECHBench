import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Central attractor term - global minimum at origin
        attractor_term = np.sum(x**2)
        
        # Chaotic sinusoidal components with varying frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Nested oscillations creating multiple local minima
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (x[i] - np.sin(x[i]))**2
        
        # Combine terms with different weights
        return 0.5 * attractor_term + 0.3 * chaotic_term + 0.2 * nested_term