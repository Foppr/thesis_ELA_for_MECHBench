import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic sine modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 4.0) * (1.0 + 0.7 * np.sin(r * 3.0) * np.cos(r * 0.8))
        
        # Sinusoidal chaos component with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi * (i + 2.0)) * np.exp(-x[i]**2 / 10.0)
        
        # Higher-order polynomial interactions with cross-dimensional coupling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**4 + 0.5 * x[i]**6 + 0.3 * x[i]**3
        
        # Cross-dimensional interaction with trigonometric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.7) * (1.0 + 0.2 * (x[i]**2 + x[j]**2))
        
        # Additional angular-based symmetry breaking
        angle_term = 0.0
        for i in range(self.dim):
            angle_term += np.sin(x[i] * np.pi / 3.0) * np.cos(x[i] * np.pi / 4.0)
        
        # Novel exponential decay component
        exp_decay_term = 0.0
        for i in range(self.dim):
            exp_decay_term += np.exp(-np.abs(x[i]) / 2.0) * np.sin(x[i] * 2.0)
        
        # Combine all terms with different weights
        result = radial_term + 0.7 * chaotic_term + 0.5 * poly_term + 0.4 * cross_term + 0.2 * angle_term + 0.1 * exp_decay_term
        
        return result