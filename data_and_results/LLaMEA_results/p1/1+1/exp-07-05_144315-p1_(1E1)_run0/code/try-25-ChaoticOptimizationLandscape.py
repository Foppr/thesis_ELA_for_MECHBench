import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Sinusoidal perturbations with modified frequencies
        sin_perturbation = np.sum(np.sin(15 * x) * np.cos(5 * x))
        
        # Exponential decay terms with different coefficients
        exp_decay = np.sum(np.exp(-0.3 * x**2) * np.sin(5 * x))
        
        # Chaotic component with cubic interactions
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic += np.sin(x[i] * x[i+1]**2) * np.exp(-0.15 * (x[i]**2 + x[i+1]**2))
        
        # Add cubic term for increased nonlinearity
        cubic_term = 0.1 * np.sum(x**3)
        
        # Add a global scaling factor with modified influence
        scaling = 1.0 + 0.15 * np.sum(np.abs(x))
        
        return quadratic + 0.6 * sin_perturbation + 0.4 * exp_decay + 0.25 * chaotic + cubic_term + scaling