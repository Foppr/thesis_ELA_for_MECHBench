import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component with multiple frequencies and phase shifts
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + np.cos(3 * np.pi * x_scaled) + 
                          0.5 * np.sin(4 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Exponential decay component with adaptive weights
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * (np.sin(5 * x_scaled) + 0.3 * np.cos(7 * x_scaled)))
        
        # Enhanced polynomial term with higher degrees, mixed interactions, and non-integer exponents
        poly_term = np.sum(x_scaled**5 + 0.3 * x_scaled**3 + 0.5 * x_scaled**2 + 
                          0.1 * np.abs(x_scaled)**1.5 + 0.05 * x_scaled**6)
        
        # Chaotic component with nested sine and cosine interactions
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.2 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) + 
                             0.1 * np.sin(x_scaled**3) * np.cos(x_scaled**2))
        
        # Additional interaction term between dimensions with variable coupling
        interaction_term = np.sum(np.sin(x_scaled[:-1] - x_scaled[1:]) * 
                                np.cos(x_scaled[:-1] + x_scaled[1:]) * 
                                (1 + 0.2 * np.sin(3 * x_scaled[:-1])))
        
        # Cross-dimensional polynomial interactions
        cross_term = np.sum((x_scaled[:-1] + x_scaled[1:])**4 + 
                           0.5 * (x_scaled[:-1] - x_scaled[1:])**3)
        
        # Combine all terms with optimized weights and add a global offset
        return 0.2 * trig_term + 0.3 * exp_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.1 * interaction_term + 0.05 * cross_term + 1.5