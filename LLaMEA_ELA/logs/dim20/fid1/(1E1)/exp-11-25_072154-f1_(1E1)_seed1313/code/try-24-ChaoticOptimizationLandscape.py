import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (1 + 0.5 * np.sin(7 * r))
        
        # Trigonometric oscillations in each dimension with higher frequency
        trig = np.sum(np.cos(4 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Exponential interaction terms between dimensions with cubic nonlinearity
        exp_interaction = np.sum(np.exp(-0.3 * (x_scaled[:-1] - x_scaled[1:])**3))
        
        # Chaotic component using sine of squared distances with different frequency
        chaotic = np.sum(np.sin(12 * r**2) * np.cos(9 * r**2))
        
        # Add cubic terms for increased nonlinearity
        cubic = np.sum(x_scaled**3)
        
        # Combine all components with different weights
        return 0.3 * radial + 0.25 * trig + 0.25 * exp_interaction + 0.15 * chaotic + 0.05 * cubic