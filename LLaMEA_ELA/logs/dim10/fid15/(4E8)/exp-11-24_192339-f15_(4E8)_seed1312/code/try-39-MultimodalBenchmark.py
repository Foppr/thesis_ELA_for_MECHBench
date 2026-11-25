import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(np.pi * x[i] * (i + 1)) * np.cos(2 * np.pi * x[i] * (i + 1))
        
        # Polynomial interaction terms creating complex valleys
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] - x[j])**4 + (x[i] + x[j])**2
        
        # Logarithmic barrier to prevent boundary escape and create narrow channels
        log_barrier = 0
        for i in range(self.dim):
            log_barrier -= np.log(25.0 - x[i]**2)
        
        # Combine all components with different weights
        return 0.3 * chaotic + 0.4 * poly_interaction + 0.3 * log_barrier