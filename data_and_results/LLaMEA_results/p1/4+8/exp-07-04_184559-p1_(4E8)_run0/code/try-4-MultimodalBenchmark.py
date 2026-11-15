import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Product of sinusoidal terms to create multiple local minima
        sinusoidal = np.prod(np.sin(5 * np.pi * x_norm))
        
        # Add a penalty term for large values to encourage convergence to origin
        penalty = 0.1 * np.sum(x_norm**4)
        
        # Combine terms to create a challenging landscape
        return quadratic + 10 * sinusoidal + penalty