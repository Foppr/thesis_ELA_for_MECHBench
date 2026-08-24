import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        sinusoidal = np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Additional penalty term to encourage convergence to origin
        penalty = 0.1 * np.sum(x_normalized**4)
        
        return quadratic + sinusoidal + penalty