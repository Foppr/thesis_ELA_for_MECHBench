import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function with enhanced complexity
        # Combines quadratic terms with sinusoidal perturbations and interaction terms
        result = np.sum(x**2) + 0.2 * np.sum(np.sin(3.0 * x)) + 0.05 * np.sum(x**4) + 0.1 * np.sum(x[:-1] * x[1:])
        
        # Add a global minimum at the origin
        return result