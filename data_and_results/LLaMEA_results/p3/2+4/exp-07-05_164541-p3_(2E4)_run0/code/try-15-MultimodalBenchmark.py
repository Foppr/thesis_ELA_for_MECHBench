import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Combines quadratic terms with sinusoidal perturbations and cubic terms
        result = np.sum(x**2) + 0.15 * np.sum(np.sin(7 * x)) + 0.02 * np.sum(x**4) + 0.05 * np.sum(x**3)
        
        # Add a global minimum at the origin
        return result