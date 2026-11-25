import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential terms
        exp_potential = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.0 * np.pi * x))
        
        # Trigonometric wave interactions with varying frequencies
        trig_waves = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Adaptive ridge functions with variable steepness
        ridge = 0.0
        for i in range(self.dim):
            ridge += (x[i] ** 2) * np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-term interactions with sinusoidal modulation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                
        # Asymmetric penalty for values near boundaries
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.0, np.exp(np.abs(x) - 4.0), 0.0))
        
        # Add a global scaling factor to control the function's range
        return 0.3 * exp_potential + 0.4 * trig_waves + 0.2 * ridge + 0.05 * cross_terms + 0.05 * boundary_penalty