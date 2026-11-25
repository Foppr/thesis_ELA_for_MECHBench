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
        trig_interfere = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x))
        
        # Radial symmetry breaking term
        radial_break = np.sum((x**2) * np.sin(0.5 * np.sqrt(np.sum(x**2))))
        
        # Cross-dimensional cubic couplings
        cubic_coupling = 0.1 * np.sum((x[:-1] * x[1:]) ** 3)
        
        # Additional chaotic sinusoidal component
        chaotic_component = 0.05 * np.sum(np.sin(7.0 * x + np.sin(2.0 * x)))
        
        # Combine all terms
        result = exp_term + trig_interfere + radial_break + cubic_coupling + chaotic_component
        
        return result