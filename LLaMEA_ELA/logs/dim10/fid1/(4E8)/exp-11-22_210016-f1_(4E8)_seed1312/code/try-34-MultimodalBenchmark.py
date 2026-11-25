import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher-order components
        poly_term = 0.4 * np.sum(x**2) + 0.05 * np.sum(x**4) + 0.02 * np.sum(x**5) + 0.005 * np.sum(x**6)
        
        # Enhanced sinusoidal oscillations with increased frequency
        sin_term = np.sum(np.sin(12.0 * x) + 0.5 * np.sin(24.0 * x))
        
        # Modified cross-term interaction with different weighting
        cross_term = 0.3 * np.sum(x[:-1] * x[1:])
        
        # Additional quadratic cross-term for increased complexity
        quad_cross = 0.2 * np.sum((x[:-1] + x[1:]) ** 2)
        
        # Cubic cross-term interaction with altered coefficients
        cubic_cross = 0.1 * np.sum(x[:-2] * x[1:-1] * x[2:])
        
        # Additional quartic cross-term for higher complexity
        quartic_cross = 0.05 * np.sum((x[:-3] + x[1:-2] + x[2:-1] + x[3:]) ** 4)
        
        # Mixed trigonometric and polynomial interaction
        mixed_term = 0.15 * np.sum(np.sin(x) * x**2)
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + quad_cross + cubic_cross + quartic_cross + mixed_term
        
        return result