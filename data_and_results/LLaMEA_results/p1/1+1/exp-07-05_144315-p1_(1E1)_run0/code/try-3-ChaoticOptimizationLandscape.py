import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Sinusoidal perturbations with varying frequencies
        sin_perturbation = np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        # Exponential decay terms that create rugged terrain
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(3 * x))
        
        # Chaotic component using a logistic map-like structure
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic += np.sin(x[i] * x[i+1]) * np.exp(-0.1 * (x[i] + x[i+1])**2)
        
        # Add a global scaling factor to control the landscape difficulty
        scaling = 1.0 + 0.1 * np.sum(np.abs(x))
        
        return quadratic + 0.5 * sin_perturbation + 0.3 * exp_decay + 0.2 * chaotic + scaling