import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Highly chaotic sine-wave component with multiple frequencies and nonlinear modulation
        sine_term = np.sum(np.sin(5 * np.pi * x_norm) * np.sin(13 * np.pi * x_norm) * 
                          np.sin(17 * np.pi * x_norm) + 0.3 * np.sin(9 * np.pi * x_norm) * 
                          np.sin(23 * np.pi * x_norm))
        
        # Spherical radial component with higher-order polynomial terms
        radial_term = np.sum(x_norm ** 4 + 0.2 * (x_norm ** 6) + 0.05 * (x_norm ** 8))
        
        # Long-range dimensional coupling with exponential decay and chaotic modulation
        coupling_term = 0.2 * np.sum(np.exp(-2.0 * (x_norm[:-2] - x_norm[2:]) ** 2) * 
                                   (x_norm[:-2] ** 2 + x_norm[2:] ** 2) * 
                                   np.sin(3 * np.pi * (x_norm[:-2] + x_norm[2:])))
        
        # Nonlinear interaction terms with chaotic phase shifts and multi-dimensional coupling
        interaction_term = 0.4 * np.sum(np.sin(4 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      np.cos(7 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                      (x_norm[:-1] ** 4 + x_norm[1:] ** 4))
        
        # Additional chaotic component with fractal-like behavior
        fractal_term = 0.15 * np.sum(np.abs(x_norm) ** 1.7 * np.sin(11 * np.pi * x_norm))
        
        # Combined function with complex weighting scheme
        result = 3.2 * sine_term + 1.1 * radial_term + 0.8 * coupling_term + 0.5 * interaction_term + 0.25 * fractal_term
        
        return result