import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced trigonometric component with multiple frequencies and modulation
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + 
                          np.cos(3 * np.pi * x_scaled) + 
                          0.5 * np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Exponential decay component with quadratic modulation for steeper gradients
        exp_term = np.sum(np.exp(-np.abs(x_scaled)**2) * np.sin(5 * x_scaled) * np.cos(2 * x_scaled))
        
        # Higher-order polynomial term for increased nonlinearity and complexity
        poly_term = np.sum(x_scaled**6 + 0.7 * x_scaled**4 + 0.3 * x_scaled**2)
        
        # Chaotic component with mixed sinusoidal and polynomial interactions
        chaotic_term = np.sum(np.sin(x_scaled**3) * np.cos(x_scaled**2) + 
                             0.5 * np.sin(x_scaled)**3 * np.cos(x_scaled))
        
        # Add coupling between dimensions to increase interdependence
        coupling = np.sum((x_scaled[:-1] - x_scaled[1:])**2)
        
        # Combine all terms with different weights and add constant offset
        return 0.25 * trig_term + 0.35 * exp_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.05 * coupling + 1.5