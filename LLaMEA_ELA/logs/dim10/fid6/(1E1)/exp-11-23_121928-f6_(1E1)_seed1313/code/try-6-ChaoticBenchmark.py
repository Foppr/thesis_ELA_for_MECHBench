import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component creating oscillations
        trig_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential barrier terms creating steep gradients
        exp_term = np.sum(np.exp(-x_scaled**2 / 2.0) * (1 + 0.5 * np.sin(15 * x_scaled)))
        
        # Polynomial interaction term creating complex curvature
        poly_term = np.sum(x_scaled**4 + 0.3 * x_scaled**3 - 0.1 * x_scaled**2)
        
        # Chaotic component using sine of exponential
        chaotic_term = np.sum(np.sin(np.exp(x_scaled)) * np.cos(np.exp(-x_scaled)))
        
        # Combined function with multiple competing forces
        return 2.0 * trig_term + 0.5 * exp_term + 0.3 * poly_term + 0.1 * chaotic_term + 0.01 * np.sum(x_scaled**6)