import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with different frequencies
        sinusoidal = np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Product of all dimensions (creates correlation between variables)
        product = np.prod(x_normalized)
        
        # Combined function with multiple local minima
        return quadratic + 0.1 * sinusoidal + 0.01 * product