import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple local minima
        f2 = 0.1 * np.sum(np.sin(7 * np.pi * x_normalized))
        
        # Product term creating complex landscape
        f3 = np.prod(np.cos(1.5 * x_normalized))
        
        # Additional interaction term with modified coupling
        f4 = 0.05 * np.sum(x_normalized**3)
        
        # New coupling term between dimensions using sine function
        coupling_term = 0.2 * np.sum(np.sin(3 * np.pi * (x_normalized[:-1] + x_normalized[1:])))
        
        # Combined function with multiple peaks and valleys
        return f1 + f2 + 0.6 * f3 + f4 + 0.1 * np.sum(x_normalized**4) + coupling_term