import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with chaotic modulation
        exp_term = np.sum(np.exp(-0.1 * np.abs(x)) * np.cos(2.0 * np.pi * x))
        
        # Trigonometric interference with varying frequencies
        trig_term = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x))
        
        # Radial symmetry breaking term
        radial_break = np.sum((x**2 + 0.1 * np.sin(x)) ** 2)
        
        # Cross-dimensional cubic couplings
        cubic_coupling = 0.05 * np.sum((x[:-1] ** 3 + x[1:] ** 3) * (x[:-1] + x[1:]))
        
        # Additional chaotic component
        chaotic_component = 0.2 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)))
        
        # Combine all terms
        result = exp_term + trig_term + radial_break + cubic_coupling + chaotic_component
        
        return result