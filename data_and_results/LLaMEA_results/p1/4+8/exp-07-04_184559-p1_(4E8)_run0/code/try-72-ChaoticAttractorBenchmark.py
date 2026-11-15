import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for chaotic logistic map
        self.r = 3.95
        self.x0 = 0.5
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial potential terms
        poly_potential = np.sum(x_norm**4) - 2 * np.sum(x_norm**2)
        
        # Trigonometric coupling terms
        trig_coupling = np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Cross-dimensional interaction using a chaotic logistic map
        chaotic_term = 0.0
        if self.dim > 1:
            x_prev = self.x0
            for i in range(min(10, self.dim)):
                x_prev = self.r * x_prev * (1 - x_prev)
                if i < len(x_norm):
                    chaotic_term += x_norm[i] * x_prev
        
        # Add a global ruggedness term using a sum of sinusoids with varying frequencies
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sum(np.sin((i+1) * x_norm) * np.cos((i+1) * x_norm))
        
        # Combine all components
        return poly_potential + 1.5 * trig_coupling + 0.5 * chaotic_term + 0.3 * ruggedness