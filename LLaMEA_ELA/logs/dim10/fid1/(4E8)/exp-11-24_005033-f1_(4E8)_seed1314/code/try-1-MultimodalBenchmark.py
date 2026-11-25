import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Sum of quadratic terms with different scales and offsets
        result = 0.0
        
        # Global minimum at origin (0,0,...,0) with value 0
        # Multiple local minima scattered throughout the domain
        for i in range(self.dim):
            # Quadratic term with different coefficients
            result += (x[i] - 1.0)**2 * (1.0 + 0.1 * np.sin(10.0 * x[i]))
            
        # Add a sinusoidal component to create multiple local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Add a small noise term to make it more challenging
        result += 0.01 * np.sum(x**2)
        
        return result