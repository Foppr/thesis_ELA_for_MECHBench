import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 3.0) * (1.0 + 0.7 * np.sin(1.5 * r))
        
        # Trigonometric interference pattern with altered frequencies
        trig_term = np.sum(np.cos(4.0 * x) * np.sin(1.5 * x))
        
        # Chaotic component using sine maps with modified coupling
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += np.sin(1.2 * x[i] * x[i+1]) * np.cos(0.8 * (x[i] + x[i+1]))
        
        # Cross-term interaction with cubic coupling and varying weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i]**3 * x[j]) / (1.0 + np.abs(x[i] - x[j])**2)
        
        # Combine all terms with different weights
        result = radial_term + trig_term + 0.4 * chaotic_term + 0.15 * cross_term
        
        return result