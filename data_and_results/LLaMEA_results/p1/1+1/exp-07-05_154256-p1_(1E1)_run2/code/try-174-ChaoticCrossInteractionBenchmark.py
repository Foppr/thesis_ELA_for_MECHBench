import numpy as np

class ChaoticCrossInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 2.0
        self.c2 = 3.0
        self.c3 = 0.5
        self.c4 = 1.5
        self.chaos_factor = 4.1
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_term = self.c1 * r**2 + self.c2 * r**4 + self.c3 * r**6
        
        # Sinusoidal oscillation in each dimension
        sin_term = 0
        for i in range(self.dim):
            sin_term += np.sin(self.chaos_factor * x[i]) * np.cos(self.chaos_factor * x[i] * 0.7)
        
        # Cross-dimensional interaction with chaotic modulation
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction using a modified logistic map
                chaotic_val = np.sin(self.chaos_factor * x[i] * x[j]) * np.cos(self.chaos_factor * x[i] * x[j] * 0.3)
                cross_term += chaotic_val * (x[i]**2 + x[j]**2)
        
        # Additional polynomial interaction with radial dependence
        poly_interaction = 0
        for i in range(self.dim):
            poly_interaction += x[i]**3 * np.sin(self.c4 * r)
        
        # Final combined function with adaptive scaling
        return radial_term + 2.5 * sin_term + 0.8 * cross_term + 0.3 * poly_interaction