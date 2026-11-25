import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2 * 0.5) * (1 + 0.3 * np.sin(7 * r))
        
        # Enhanced trigonometric oscillations in each dimension
        trig = np.sum(np.cos(4 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Cross-dimensional interaction terms with different weights
        cross_interaction = 0
        for i in range(self.dim - 1):
            cross_interaction += np.exp(-0.3 * (x_scaled[i] - x_scaled[i+1])**2) * np.sin(2 * np.pi * (x_scaled[i] + x_scaled[i+1]))
        
        # Chaotic component with higher frequency oscillations
        chaotic = np.sum(np.sin(15 * r**2) * np.cos(12 * r**2))
        
        # Additional nonlinear term for increased complexity
        nonlinear = np.sum(x_scaled**4) * 0.01
        
        # Combine all components with modified weights
        return 0.3 * radial + 0.4 * trig + 0.2 * cross_interaction + 0.08 * chaotic + 0.02 * nonlinear