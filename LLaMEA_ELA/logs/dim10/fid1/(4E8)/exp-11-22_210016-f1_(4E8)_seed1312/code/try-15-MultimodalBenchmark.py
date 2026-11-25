import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Higher-order polynomial terms for increased complexity
        poly_term = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Modified sinusoidal oscillations with varying frequencies
        sin_term = np.sum(np.sin(3.0 * x)) + 0.5 * np.sum(np.sin(7.0 * x))
        
        # Enhanced cross-term interactions
        cross_term = np.sum(x[:-1] * x[1:]) + 0.1 * np.sum(x[:-2] * x[2:])
        
        # Additional quadratic interaction terms
        quad_interaction = np.sum((x[:-1] - x[1:])**2)
        
        # Combine all terms with adjusted weights
        result = poly_term + sin_term + 0.5 * cross_term + 0.3 * quad_interaction
        
        return result