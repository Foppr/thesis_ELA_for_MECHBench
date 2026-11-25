import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with modified coefficients
        poly_term = 0.4 * np.sum(x**2) + 0.05 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with different frequencies and phases
        sin_term = np.sum(np.sin(11.0 * x) * np.cos(7.0 * x))
        
        # Cross-term interaction with different weighting and higher-order terms
        cross_term = 0.25 * np.sum(x[:-1] * x[1:]) + 0.1 * np.sum((x[:-1] * x[1:])**2)
        
        # Additional cubic cross-term for increased complexity
        cubic_cross = 0.2 * np.sum((x[:-1] + x[1:]) ** 3) + 0.05 * np.sum((x[:-1] - x[1:]) ** 3)
        
        # Radial symmetry component to increase non-convexity
        radial_term = 0.1 * np.sum(x**2)**2
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + cubic_cross + radial_term
        
        return result