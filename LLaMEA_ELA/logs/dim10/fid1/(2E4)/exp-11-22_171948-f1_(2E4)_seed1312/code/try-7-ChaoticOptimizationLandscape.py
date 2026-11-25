import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Exponential decay terms creating steep gradients
        exp_decay = np.sum(np.exp(-x_scaled**2) - 1.0)
        
        # Periodic perturbations with varying frequencies
        periodic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Chaotic component using sine of exponential
        chaotic = np.sum(np.sin(np.exp(x_scaled)) + np.cos(np.exp(-x_scaled)))
        
        # Combined function with different weights
        result = quadratic + 0.5 * exp_decay + 0.3 * periodic + 0.2 * chaotic
        
        return result