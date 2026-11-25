import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple local minima and altered frequency
        f2 = 0.2 * np.sum(np.sin(9 * np.pi * x_normalized))
        
        # Product term creating complex landscape with modified amplitude
        f3 = 0.5 * np.prod(np.cos(x_normalized))
        
        # Additional interaction term for increased complexity
        f4 = 0.08 * np.sum(x_normalized**3)
        
        # Combined function with multiple peaks and valleys
        return f1 + f2 + f3 + f4 + 0.15 * np.sum(x_normalized**4)