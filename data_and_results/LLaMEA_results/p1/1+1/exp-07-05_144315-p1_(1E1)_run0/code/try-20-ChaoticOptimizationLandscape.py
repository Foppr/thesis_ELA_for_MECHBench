import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Multiple sinusoidal perturbations with varying frequencies and amplitudes
        sin_perturbation = (np.sum(np.sin(20 * x) * np.cos(7 * x)) + 
                           0.5 * np.sum(np.sin(12 * x) * np.cos(3 * x)) + 
                           0.3 * np.sum(np.sin(8 * x) * np.cos(11 * x)))
        
        # Exponential decay terms with different coefficients and interaction patterns
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(7 * x) * np.cos(2 * x))
        
        # Chaotic component with higher-order interactions and cross-dimensional coupling
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic += (np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * 
                           np.exp(-0.2 * (x[i]**2 + x[j]**2)) * 
                           np.sin(0.5 * (x[i] + x[j])**3))
        
        # Higher-order polynomial terms for increased nonlinearity
        cubic_term = 0.15 * np.sum(x**3)
        quartic_term = 0.05 * np.sum(x**4)
        
        # Cross-dimensional interaction with trigonometric coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_interaction += np.sin(x[i] * np.cos(x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Global scaling factor with chaotic influence
        scaling = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(np.sin(x)**2)
        
        # Add a complex interaction term that creates many local optima
        complex_interaction = 0.3 * np.sum(np.sin(3 * x) * np.cos(5 * x) * np.exp(-0.1 * np.abs(x)))
        
        return (quadratic + 0.8 * sin_perturbation + 0.5 * exp_decay + 
                0.4 * chaotic + cubic_term + quartic_term + 0.3 * cross_interaction + 
                complex_interaction + scaling)