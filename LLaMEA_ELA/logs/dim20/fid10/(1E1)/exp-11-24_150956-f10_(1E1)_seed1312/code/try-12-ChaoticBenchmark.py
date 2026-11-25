import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested trigonometric components with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + 
                          np.cos(3 * np.pi * x_scaled) + 
                          0.5 * np.sin(7 * np.pi * x_scaled) + 
                          0.3 * np.cos(11 * np.pi * x_scaled))
        
        # Fractional polynomial terms to create non-smooth gradients
        poly_term = np.sum(x_scaled**(5/2) + 0.4 * x_scaled**(3/2) + 0.6 * x_scaled**(1/2))
        
        # Exponential decay with sinusoidal modulation
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * (np.sin(5 * x_scaled) + 0.5 * np.cos(8 * x_scaled)))
        
        # Chaotic logistic map component with dimension interactions
        chaotic_term = np.sum(np.sin(np.pi * x_scaled**2) * np.cos(np.pi * x_scaled) + 
                             0.3 * np.sin(4 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) +
                             0.1 * np.sin(9 * np.pi * x_scaled**2))
        
        # Cross-dimensional interaction with nested sine waves
        interaction_term = np.sum(np.sin(x_scaled[:-1] - x_scaled[1:]) * 
                                np.cos(x_scaled[:-1] + x_scaled[1:]) * 
                                np.sin(0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Additional chaotic component using a modified logistic map
        logistic_component = np.sum(4 * x_scaled * (1 - x_scaled) + 
                                  0.2 * np.sin(np.pi * x_scaled) * np.cos(np.pi * x_scaled))
        
        # Combine all terms with different weights and add a global offset
        return (0.3 * trig_term + 
                0.25 * poly_term + 
                0.2 * exp_term + 
                0.15 * chaotic_term + 
                0.05 * interaction_term + 
                0.05 * logistic_component + 
                3.0)