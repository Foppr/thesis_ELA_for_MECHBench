import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function with enhanced complexity
        # Combines quadratic terms with sinusoidal perturbations and higher-order terms
        result = np.sum(x**2) + 0.1 * np.sum(np.sin(5.0 * x)) + 0.01 * np.sum(x**4) + 0.001 * np.sum(np.cos(10.0 * x))
        
        # Add additional complexity with product terms to increase landscape difficulty
        if self.dim > 1:
            product_term = np.sum(x[:-1] * x[1:])
            result += 0.05 * product_term
            
        # Add a global minimum at the origin
        return result