import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with varying frequencies
        sin_perturbation = np.sum(np.sin(20 * x) * np.cos(7 * x) * np.sin(3 * x))
        
        # Modified exponential decay with stronger interaction
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.cos(6 * x) * np.sin(2 * x))
        
        # Enhanced chaotic component with higher-order interactions
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic += np.sin(x[i] * x[i+1]**3) * np.exp(-0.2 * (x[i]**2 + x[i+1]**2))
            if i < self.dim - 2:
                chaotic += 0.5 * np.cos(x[i] * x[i+1] * x[i+2]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2 + x[i+2]**2))
        
        # Strengthened cubic term with cross-terms
        cubic_term = 0.15 * np.sum(x**3) + 0.05 * np.sum(x**2 * np.sin(x))
        
        # Global scaling with enhanced nonlinearity
        scaling = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(x**4)
        
        # Add a small noise component to increase problem complexity
        noise = 0.01 * np.sum(np.sin(100 * x))
        
        return quadratic + 0.7 * sin_perturbation + 0.5 * exp_decay + 0.3 * chaotic + cubic_term + scaling + noise