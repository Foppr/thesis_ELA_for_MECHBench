import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with modified exponential decay and symmetry breaking
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.5) * (1.0 + 0.4 * np.sin(r * 1.2) + 0.15 * np.cos(r * 2.5))
        
        # Higher-order trigonometric interference pattern with adjusted frequencies
        trig_term = np.sum(np.cos(6.0 * x) * np.sin(3.5 * x) + np.sin(3.5 * x) * np.cos(1.8 * x))
        
        # Chaotic component using sine maps with quadratic coupling and altered weights
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1]) * (1.0 + 0.15 * x[i]**2)
        
        # Cross-term interaction with stronger cubic couplings and variable weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j] * (x[i] + x[j])**2) / (1.0 + np.abs(x[i] - x[j])**3)
        
        # Additional cubic polynomial interactions with modified coefficients
        cubic_term = 0.0
        for i in range(self.dim):
            cubic_term += 0.07 * x[i]**3
        
        # Combine all terms with different weights
        result = radial_term + trig_term + 0.5 * chaotic_term + 0.2 * cross_term + 0.25 * cubic_term
        
        return result