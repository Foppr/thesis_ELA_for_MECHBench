import numpy as np

class ChaoticCubicLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic cubic polynomial terms with varying coefficients
        cubic_terms = 0
        for i in range(self.dim):
            coeff = 1.5 + 0.8 * np.sin(1.3 * i + 0.7)
            cubic_terms += coeff * x[i]**3
        
        # Saddle point structure via coupled quadratic terms
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimensionality
                coeff = 0.5 + 0.3 * np.cos(0.9 * (i - j) + 1.1)
                saddle += coeff * x[i]**2 * x[j]
        
        # Non-separable interaction with sinusoidal modulation
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = np.sin(0.5 * (x[i] + x[j]) + 0.8)
                interaction += (x[i]**2 + x[j]**2) * mod
        
        # Dynamic scaling based on position
        scaling = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(2.0 * x[i] + 0.3)
            scaling += scale_factor * x[i]**2
        
        # Combine all components with different weights
        return 0.8 * cubic_terms + 0.6 * saddle + 0.7 * interaction + 1.2 * scaling