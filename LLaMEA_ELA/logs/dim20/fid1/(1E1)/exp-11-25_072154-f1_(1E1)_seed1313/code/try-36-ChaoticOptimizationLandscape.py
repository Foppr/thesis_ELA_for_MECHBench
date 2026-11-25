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
        
        # Trigonometric oscillations in each dimension with modified frequencies
        trig = np.sum(np.cos(4 * np.pi * x_scaled) * np.sin(6 * np.pi * x_scaled))
        
        # Exponential interaction terms between dimensions with cubic nonlinearity
        exp_interaction = np.sum(np.exp(-0.5 * (x_scaled[:-1]**3 - x_scaled[1:]**3)**2))
        
        # Chaotic component using sine of squared distances with different frequency
        chaotic = np.sum(np.sin(12 * r**2) * np.cos(8 * r**2))
        
        # Add a new cubic polynomial term for additional complexity
        cubic_term = np.sum(x_scaled**3)
        
        # Combine all components with different weights
        return 0.3 * radial + 0.3 * trig + 0.2 * exp_interaction + 0.15 * chaotic + 0.05 * cubic_term