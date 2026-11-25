import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squared terms with different scales
        term1 = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal components
        term2 = 0.1 * np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Add a smooth quadratic term that creates a global minimum at origin
        term3 = 0.01 * np.sum(x_normalized**4)
        
        # Combine all terms to create a challenging landscape
        return term1 + term2 + term3