import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave component with non-linear frequency modulation
        sine_term = np.sum(np.sin(5 * np.pi * x_norm) * np.sin(13 * np.pi * x_norm) * 
                          np.sin(21 * np.pi * x_norm) + 0.3 * np.sin(9 * np.pi * x_norm))
        
        # Enhanced radial component with exponential and polynomial terms
        radial_term = np.sum(np.exp(2 * x_norm) - 1 + 0.2 * (x_norm ** 4) + 0.05 * (x_norm ** 6))
        
        # Long-range cross-dimensional coupling with power-law decay
        coupling_term = 0.2 * np.sum(np.abs(x_norm[:-2] - x_norm[2:]) ** (-1.5) * 
                                   (x_norm[:-2] ** 2 + x_norm[2:] ** 2))
        
        # Nonlinear interaction terms with chaotic modulation
        interaction_term = 0.3 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      np.cos(7 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                      (x_norm[:-1] ** 4 + x_norm[1:] ** 4))
        
        # Additional chaotic component with mixed trigonometric functions
        chaotic_term = 0.15 * np.sum(np.tan(0.5 * np.pi * x_norm) * np.cosh(x_norm) * 
                                   np.sinh(x_norm))
        
        # Combined function with varying weights and enhanced complexity
        result = 3.0 * sine_term + 1.2 * radial_term + 0.8 * coupling_term + 0.5 * interaction_term + 0.4 * chaotic_term
        
        return result