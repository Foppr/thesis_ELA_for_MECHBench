import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Polynomial terms
        poly_term = np.sum(x**4 - 16*x**2 + 5*x)
        
        # Sinusoidal oscillations
        sin_term = np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Additional multimodal components
        multi_term = np.sum(np.exp(-0.1 * (x - 2)**2) + np.exp(-0.1 * (x + 2)**2))
        
        # Combine all terms with different weights
        result = 0.1 * poly_term + 0.5 * sin_term - 0.3 * multi_term
        
        return result