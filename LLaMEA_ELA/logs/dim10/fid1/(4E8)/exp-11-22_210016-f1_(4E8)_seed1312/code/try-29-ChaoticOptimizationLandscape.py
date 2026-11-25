import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 5.0) * (1.0 + 0.5 * np.sin(r))
        
        # Trigonometric interference pattern
        trig_term = np.sum(np.cos(3.0 * x) * np.sin(2.0 * x))
        
        # Chaotic component using sine maps
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
        
        # Cross-term interaction with varying weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j]))
        
        # Combine all terms with different weights
        result = radial_term + trig_term + 0.3 * chaotic_term + 0.1 * cross_term
        
        return result