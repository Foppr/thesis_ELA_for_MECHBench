import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function value
        # Combines quadratic terms with sinusoidal perturbations
        # to create multiple local minima
        result = np.sum(x**2) + 0.1 * np.sum(np.sin(5 * x)) + 0.01 * np.sum(x**4)
        
        return result