import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with modified frequencies
        f2 = 0.15 * np.sum(np.sin(7.0 * x) * np.exp(-0.15 * x**2))
        
        # Add a global minimum at origin with additional attractive terms
        f3 = 0.02 * np.sum(np.cos(12.0 * x) * np.exp(-0.07 * x**2))
        
        # Add a shifted quadratic basin to increase complexity
        shifted_x = x - 0.5
        f4 = 0.05 * np.sum(shifted_x**2 * np.exp(-0.02 * shifted_x**2))
        
        return f1 + f2 + f3 + f4