import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with polynomial chaos
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.3 * np.sin(7 * r) * np.cos(4 * r)) * np.exp(-r**3)
        
        # Polynomial interaction terms with higher order
        poly_interaction = np.sum((x_scaled**4 - 2 * x_scaled**2 + 1)**2)
        
        # Cross-dimensional coupling with sine modulation
        cross_coupling = np.sum(np.sin(2 * np.pi * x_scaled[:-1]) * np.cos(3 * np.pi * x_scaled[1:]))
        
        # Multi-scale trigonometric oscillations
        trig_oscillations = np.sum(np.sin(15 * x_scaled) + 0.5 * np.cos(8 * x_scaled))
        
        # Chaotic component with exponential decay and sinusoidal modulation
        chaotic = np.exp(-r**2) * np.sin(12 * r) * np.cos(5 * r)
        
        # Combine all components with different weights
        return 0.3 * radial + 0.25 * poly_interaction + 0.2 * cross_coupling + 0.15 * trig_oscillations + 0.1 * chaotic