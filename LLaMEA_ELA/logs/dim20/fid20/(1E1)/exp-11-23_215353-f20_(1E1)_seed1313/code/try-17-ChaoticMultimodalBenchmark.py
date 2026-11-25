import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term
        exp_term = np.sum(np.exp(-0.5 * x**2))
        
        # Trigonometric modulation with varying frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Polynomial distortion with random coefficients
        poly_term = np.sum((x**3 + 0.5 * x**2 - 0.3 * x + 1.0)**2)
        
        # Chaotic component using sine of exponential
        chaotic_term = np.sum(np.sin(np.exp(x)))
        
        # Combine all terms with different weights
        return 0.5 * exp_term + 0.3 * trig_term + 0.2 * poly_term + 0.1 * chaotic_term + 2.0