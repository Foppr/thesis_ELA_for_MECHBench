import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial conditioning term with higher degree
        poly_term = np.sum(x_scaled**8 - 4*x_scaled**6 + 3*x_scaled**4)
        
        # Nested sinusoidal oscillations with varying frequencies
        sin_term = np.sum(np.sin(25 * np.pi * x_scaled) * np.sin(15 * np.pi * x_scaled) * np.sin(7 * np.pi * x_scaled))
        
        # Exponential barrier terms to create rugged terrain
        exp_barrier = np.sum(np.exp(-3 * np.abs(x_scaled)) * np.sin(20 * np.pi * x_scaled)**2)
        
        # Cross-term interaction with different weights
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(10 * np.pi * x_scaled[:-1]) * np.cos(5 * np.pi * x_scaled[1:]))
        
        # Additional quadratic interaction term
        quad_term = np.sum((x_scaled[:-1] + x_scaled[1:]) ** 2 * np.sin(3 * np.pi * x_scaled[:-1]) * np.cos(2 * np.pi * x_scaled[1:]))
        
        # Combine all terms with different weights
        return 0.35 * poly_term + 0.3 * sin_term + 0.25 * exp_barrier + 0.08 * cross_term + 0.02 * quad_term