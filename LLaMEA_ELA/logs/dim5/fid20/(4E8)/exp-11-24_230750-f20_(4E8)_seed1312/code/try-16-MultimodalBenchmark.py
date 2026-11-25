import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms
        exp_terms = np.sum(np.exp(-0.5 * x**2))
        
        # Trigonometric interactions
        trig_terms = np.sum(np.cos(3.0 * x) * np.sin(2.0 * x))
        
        # Polynomial cross-terms with varying exponents
        poly_cross = 0.1 * np.sum(x[:-1]**3 * x[1:])
        
        # Combined function value
        return exp_terms + trig_terms + poly_cross