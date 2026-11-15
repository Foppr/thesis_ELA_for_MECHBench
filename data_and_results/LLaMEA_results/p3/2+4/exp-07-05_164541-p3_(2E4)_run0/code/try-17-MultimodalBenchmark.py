import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with improved conditioning
        # Combines quadratic, sinusoidal, and higher-order polynomial terms
        result = np.sum(x**2) + 0.2 * np.sum(np.sin(5 * x)**2) + 0.01 * np.sum(x**4) + 0.03 * np.sum(x**3) + 0.1 * np.sum(np.cos(3 * x))
        
        # Add a global minimum at the origin
        return result