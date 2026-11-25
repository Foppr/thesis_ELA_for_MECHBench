import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic sine modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 4.0) * (1.0 + 0.5 * np.sin(r * 2.0) * np.cos(r * 0.5))
        
        # Sinusoidal chaos component with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi * (i + 1)) * np.exp(-x[i]**2 / 10.0)
        
        # Higher-order polynomial interactions with cross-dimensional coupling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**4 + 0.3 * x[i]**6
        
        # Cross-dimensional interaction with trigonometric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * (1.0 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Additional angular-based symmetry breaking
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += np.sin(x[i] * np.pi / 2.0) * np.cos(x[i] * np.pi / 3.0)
        
        # Combine all terms with different weights
        result = radial_term + 0.5 * chaotic_term + 0.3 * poly_term + 0.2 * cross_term + 0.1 * angle_term
        
        return result