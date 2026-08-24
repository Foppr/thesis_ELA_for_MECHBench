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
        
        # Exponential decay terms with different coefficients and additional interaction
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(7 * x) * np.cos(2 * x))
        
        # Chaotic component with higher-order interactions and coupling
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                chaotic += np.sin(x[i] * x[i+1]**3 + x[i+2]**2) * np.exp(-0.2 * (x[i]**2 + x[i+1]**3 + x[i+2]**2))
        
        # Add quintic and septic terms for increased nonlinearity
        quintic_term = 0.05 * np.sum(x**5)
        septic_term = 0.02 * np.sum(x**7)
        
        # Add a global scaling factor with modified influence and additional chaotic modulation
        scaling = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(np.sin(10 * x))
        
        # Add cross-dimensional coupling with hyperbolic tangent interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.tanh(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        return quadratic + 0.8 * sin_perturbation + 0.5 * exp_decay + 0.3 * chaotic + quintic_term + septic_term + cross_coupling + scaling