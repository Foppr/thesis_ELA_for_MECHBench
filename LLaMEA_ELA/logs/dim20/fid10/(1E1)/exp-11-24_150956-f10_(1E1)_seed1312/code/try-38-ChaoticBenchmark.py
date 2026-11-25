import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced trigonometric component with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + 
                          0.7 * np.cos(3 * np.pi * x_scaled) + 
                          0.3 * np.sin(5 * np.pi * x_scaled))
        
        # Modified exponential decay with variable rate
        exp_term = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * 
                         np.sin(4 * x_scaled) * 
                         np.cos(2 * x_scaled))
        
        # Adaptive polynomial term with dimension-dependent weights
        poly_weights = np.linspace(0.1, 1.0, self.dim)
        poly_term = np.sum(poly_weights * (x_scaled**6 + 0.4 * x_scaled**4 + 0.6 * x_scaled**2))
        
        # Enhanced chaotic component with cross-dimensional interactions
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.3 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) +
                             0.1 * np.sin(6 * x_scaled**2))
        
        # Increased dimensional interaction with neighbor coupling
        if self.dim > 1:
            diff = x_scaled[:-1] - x_scaled[1:]
            sum_vals = x_scaled[:-1] + x_scaled[1:]
            interaction_term = np.sum(np.sin(diff) * np.cos(sum_vals) * 
                                   np.exp(-0.1 * np.abs(diff)))
        else:
            interaction_term = 0.0
            
        # Add a global scaling factor and noise component for increased complexity
        return (0.3 * trig_term + 
                0.25 * exp_term + 
                0.2 * poly_term + 
                0.15 * chaotic_term + 
                0.1 * interaction_term + 
                1.5 * np.random.normal(0, 0.01))