import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term
        exp_term = np.sum(np.exp(-0.3 * x**2))
        
        # Trigonometric modulation with varying frequencies
        trig_term = np.sum(np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Enhanced polynomial distortion with higher degree terms
        poly_term = np.sum((x**4 + 0.7 * x**3 - 0.4 * x**2 + 0.2 * x + 1.5)**2)
        
        # Chaotic component using sine of exponential
        chaotic_term = np.sum(np.sin(np.exp(0.5 * x)))
        
        # Additional interaction term between dimensions
        interaction_term = np.sum((x[:-1] - x[1:])**4)
        
        # Combine all terms with different weights
        return 0.4 * exp_term + 0.25 * trig_term + 0.25 * poly_term + 0.08 * chaotic_term + 0.02 * interaction_term + 2.5