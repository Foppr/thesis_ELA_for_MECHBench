import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Additional term that creates a complex landscape
        additional = np.sum(x_norm**4 - 0.5 * x_norm**2)
        
        return quadratic + 0.1 * sinusoidal + 0.01 * additional