import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (1 + 0.5 * np.sin(5 * r))
        
        # Trigonometric oscillations in each dimension
        trig = np.sum(np.cos(3 * np.pi * x_scaled) * np.sin(4 * np.pi * x_scaled))
        
        # Exponential interaction terms between dimensions
        exp_interaction = np.sum(np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2))
        
        # Chaotic component using sine of squared distances
        chaotic = np.sum(np.sin(10 * r**2) * np.cos(7 * r**2))
        
        # Combine all components with different weights
        return 0.4 * radial + 0.3 * trig + 0.2 * exp_interaction + 0.1 * chaotic