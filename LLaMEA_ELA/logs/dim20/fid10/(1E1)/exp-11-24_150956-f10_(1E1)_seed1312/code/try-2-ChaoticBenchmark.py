import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component with multiple frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + np.cos(3 * np.pi * x_scaled))
        
        # Exponential decay component to create steep gradients
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(5 * x_scaled))
        
        # Polynomial term with mixed degrees for nonlinearity
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**2)
        
        # Chaotic component using sine of squared terms
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled))
        
        # Combine all terms with different weights
        return 0.3 * trig_term + 0.4 * exp_term + 0.2 * poly_term + 0.1 * chaotic_term + 2.0