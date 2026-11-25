import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        poly_term = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with increased frequency
        sin_term = np.sum(np.sin(7.0 * x)) + 0.5 * np.sum(np.sin(3.0 * x))
        
        # Cross-term interaction with modified coefficient
        cross_term = 0.3 * np.sum(x[:-1] * x[1:]) + 0.2 * np.sum(x**2)
        
        # Additional nonlinear interaction term
        nonlinear_term = 0.1 * np.sum(np.sin(x) * np.cos(x))
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + nonlinear_term
        
        return result