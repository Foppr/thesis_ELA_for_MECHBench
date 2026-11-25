import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and enhanced symmetry
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (1 + 0.7 * np.sin(7 * r) + 0.3 * np.cos(3 * r))
        
        # Trigonometric oscillations with modified frequencies
        trig = np.sum(np.cos(4 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Exponential interaction terms between dimensions with cross-terms
        exp_interaction = np.sum(np.exp(-0.3 * (x_scaled[:-1] - x_scaled[1:])**2)) + 0.5 * np.sum(np.exp(-0.2 * (x_scaled[:-2] - x_scaled[2:])**2))
        
        # Chaotic component using sine of squared distances with higher frequency
        chaotic = np.sum(np.sin(15 * r**2) * np.cos(11 * r**2))
        
        # Add a small perturbation term to increase ruggedness
        perturbation = 0.1 * np.sum(np.sin(20 * x_scaled) * np.cos(15 * x_scaled))
        
        # Combine all components with different weights
        return 0.35 * radial + 0.25 * trig + 0.2 * exp_interaction + 0.15 * chaotic + 0.05 * perturbation