import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with modified coefficients
        poly_term = 0.4 * np.sum(x**2) + 0.05 * np.sum(x**4)
        
        # Sinusoidal oscillations with different frequency
        sin_term = np.sum(np.sin(11.0 * x))
        
        # Cross-term interaction with different weighting
        cross_term = 0.25 * np.sum(x[:-1] * x[1:])
        
        # Additional cubic cross-term for increased complexity
        cubic_cross = 0.2 * np.sum((x[:-1] + x[1:]) ** 3)
        
        # Add a radial quadratic term to increase multimodality
        radial_term = 0.1 * np.sum(x**2)**2
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + cubic_cross + radial_term
        
        return result