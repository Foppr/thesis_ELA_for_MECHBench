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
        
        # Modified exponential decay with stronger interaction
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.cos(8 * x) * np.sin(4 * x))
        
        # Enhanced chaotic component with higher-order interactions
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                chaotic += np.sin(x[i] * x[i+1] * x[i+2]) * np.exp(-0.2 * (x[i]**2 + x[i+1]**2 + x[i+2]**2))
        
        # Increased cubic term for stronger nonlinearity
        cubic_term = 0.2 * np.sum(x**3)
        
        # Additional quartic term for higher complexity
        quartic_term = 0.05 * np.sum(x**4)
        
        # Global scaling with stronger influence
        scaling = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(x**2)
        
        # Add a small noise component to increase robustness
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x)
        
        return quadratic + 0.7 * sin_perturbation + 0.5 * exp_decay + 0.3 * chaotic + cubic_term + quartic_term + scaling + noise