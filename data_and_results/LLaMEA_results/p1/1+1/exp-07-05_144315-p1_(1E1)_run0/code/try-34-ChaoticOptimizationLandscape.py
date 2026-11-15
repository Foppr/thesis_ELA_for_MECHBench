import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with multiple frequencies
        sin_perturbation = np.sum(np.sin(20 * x) * np.cos(7 * x) * np.sin(3 * x))
        
        # Exponential decay terms with different coefficients and interaction
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(8 * x) * np.cos(2 * x))
        
        # Chaotic component with higher-order interactions and coupling
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic += np.sin(x[i] * x[j]**3) * np.cos(x[i]**2 * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Add higher-order polynomial terms for increased nonlinearity
        cubic_term = 0.15 * np.sum(x**3)
        quartic_term = 0.05 * np.sum(x**4)
        
        # Add a global scaling factor with complex influence
        scaling = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(x**2)
        
        # Add a cross-term interaction between all dimensions
        cross_interaction = 0.3 * np.sum(x * np.roll(x, 1))
        
        return quadratic + 0.8 * sin_perturbation + 0.5 * exp_decay + 0.35 * chaotic + cubic_term + quartic_term + scaling + cross_interaction