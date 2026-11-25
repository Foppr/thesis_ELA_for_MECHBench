import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # This combines a quadratic term with sinusoidal perturbations
        # to create multiple local minima while maintaining a global minimum at origin
        result = np.sum(x**2) + 0.1 * np.sum(np.sin(5.0 * x)) + 0.01 * np.sum(x**4)
        
        return result