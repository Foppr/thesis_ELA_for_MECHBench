import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function with modified coefficients and added quartic terms
        result = np.sum(x**2) + 0.2 * np.sum(np.sin(5 * x)) + 0.03 * np.sum(x**4) + 0.07 * np.sum(x**3) + 0.1 * np.sum(np.sin(3 * x)**2)
        
        # Add a global minimum at the origin
        return result