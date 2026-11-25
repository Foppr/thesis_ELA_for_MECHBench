import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Higher-order polynomial terms for increased complexity
        poly_term = np.sum(0.1 * x**6 - 2.0 * x**4 + 8.0 * x**2)
        
        # Combined trigonometric oscillations with varying frequencies
        sin_term = np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) + np.sin(0.3 * x) * np.cos(0.6 * x))
        
        # Exponentially decaying barrier functions creating multiple global minima
        barrier_term = np.sum(np.exp(-0.2 * (x - 3)**2) + np.exp(-0.2 * (x + 3)**2) + 
                             0.5 * np.exp(-0.1 * (x - 1)**2) + 0.5 * np.exp(-0.1 * (x + 1)**2))
        
        # Additional coupling terms between dimensions
        coupling_term = np.sum((x[:-1] - x[1:])**2)
        
        # Combine all terms with different weights
        result = 0.15 * poly_term + 0.4 * sin_term - 0.25 * barrier_term + 0.1 * coupling_term
        
        return result