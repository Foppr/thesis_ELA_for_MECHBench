import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with modified coefficients
        poly_term = 0.25 * np.sum(x**2) + 0.04 * np.sum(x**4) + 0.015 * np.sum(x**3)
        
        # Sinusoidal oscillations with different frequency
        sin_term = np.sum(np.sin(11.0 * x))
        
        # Cross-term interaction with different weighting
        cross_term = 0.25 * np.sum(x[:-1] * x[1:])
        
        # Additional quadratic cross-term for increased complexity
        quad_cross = 0.2 * np.sum((x[:-1] + x[1:]) ** 2)
        
        # Cubic cross-term interaction
        cubic_cross = 0.07 * np.sum(x[:-2] * x[1:-1] * x[2:])
        
        # Additional quadratic term with shifted variable
        shift_term = 0.1 * np.sum((x - 1.0)**2)
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + quad_cross + cubic_cross + shift_term
        
        return result