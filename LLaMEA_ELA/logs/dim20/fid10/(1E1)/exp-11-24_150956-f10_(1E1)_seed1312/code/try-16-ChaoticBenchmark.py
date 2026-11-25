import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component with multiple frequencies
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled) + np.cos(2 * np.pi * x_scaled))
        
        # Exponential decay component to create steep gradients
        exp_term = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * np.sin(7 * x_scaled))
        
        # Enhanced polynomial term with higher degrees and mixed interactions
        poly_term = np.sum(x_scaled**6 + 0.4 * x_scaled**4 + 0.6 * x_scaled**3)
        
        # Chaotic component using sine of squared terms with interaction
        chaotic_term = np.sum(np.sin(x_scaled**2.5) * np.cos(x_scaled) + 0.3 * np.sin(5 * x_scaled) * np.cos(3 * x_scaled))
        
        # Additional interaction term between dimensions with modified frequency
        interaction_term = np.sum(np.sin(1.5 * (x_scaled[:-1] - x_scaled[1:])) * np.cos(1.5 * (x_scaled[:-1] + x_scaled[1:])))
        
        # Combine all terms with different weights
        return 0.3 * trig_term + 0.4 * exp_term + 0.2 * poly_term + 0.08 * chaotic_term + 0.02 * interaction_term + 1.5