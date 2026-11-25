import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component creating periodic structure
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Exponential component introducing steep gradients
        exp_term = np.sum(np.exp(-x_scaled**2) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Polynomial component with mixed degrees
        poly_term = np.sum(x_scaled**6 + 0.5 * x_scaled**4 - 0.3 * x_scaled**2)
        
        # Chaotic interaction term using sine of sum
        chaos_term = np.sin(np.sum(np.sin(x_scaled)) * 10) * 0.5
        
        # Combined function with diverse curvature properties
        return trig_term + exp_term + poly_term + chaos_term + 0.1 * np.sum(np.abs(x_scaled))