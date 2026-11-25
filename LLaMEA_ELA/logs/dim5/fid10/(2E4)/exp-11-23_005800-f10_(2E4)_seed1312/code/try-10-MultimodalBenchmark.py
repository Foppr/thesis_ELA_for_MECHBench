import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial penalty terms
        poly_penalty = np.sum(x**4 - 10 * x**2 + 5 * x)
        
        # Sinusoidal oscillation component creating multiple local minima
        sin_component = 0
        for i in range(self.dim):
            sin_component += np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
        
        # Chaotic modulation using logistic map-like behavior
        chaotic_mod = 0
        for i in range(self.dim):
            if i == 0:
                chaotic_mod += x[i] * np.sin(x[i] * 0.5)
            else:
                chaotic_mod += x[i] * np.sin(x[i-1] * 0.3) + x[i-1] * np.cos(x[i] * 0.4)
        
        # Combine all components with different weights
        return 0.5 * poly_penalty + 2 * sin_component + 0.1 * chaotic_mod + 5 * self.dim