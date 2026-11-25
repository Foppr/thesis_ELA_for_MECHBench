import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-0.5 * r**2) * (1 + 0.3 * np.sin(7 * r))
        
        # Trigonometric oscillations with different frequencies
        trig = np.sum(np.cos(4 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Enhanced exponential interaction terms between dimensions
        exp_interaction = np.sum(np.exp(-0.3 * (x_scaled[:-1] - x_scaled[1:])**2))
        
        # Chaotic component with modified sine and cosine frequencies
        chaotic = np.sum(np.sin(8 * r**2) * np.cos(6 * r**2))
        
        # Combine all components with different weights
        return 0.35 * radial + 0.35 * trig + 0.25 * exp_interaction + 0.05 * chaotic