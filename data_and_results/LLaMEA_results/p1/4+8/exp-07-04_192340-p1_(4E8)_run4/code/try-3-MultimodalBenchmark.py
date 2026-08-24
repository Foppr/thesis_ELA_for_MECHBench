import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Sum of quadratic terms with different coefficients
        # and sinusoidal terms to create multiple local minima
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1) + 10 * np.sin(x[i] * (i + 1))
        
        # Add a global minimum at the origin
        result += 0.1 * np.sum(x ** 2)
        
        return result