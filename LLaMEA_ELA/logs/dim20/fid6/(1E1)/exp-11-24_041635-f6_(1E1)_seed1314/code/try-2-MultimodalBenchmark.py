import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Create a highly multimodal function with exponential local minima
        # Combines quadratic, sinusoidal, and exponential terms for increased complexity
        result = np.sum(x**2) + 0.5 * np.sum(np.sin(10.0 * x)) + 0.3 * np.sum(np.exp(0.5 * np.abs(x))) + 0.05 * np.sum(x**6)
        
        return result