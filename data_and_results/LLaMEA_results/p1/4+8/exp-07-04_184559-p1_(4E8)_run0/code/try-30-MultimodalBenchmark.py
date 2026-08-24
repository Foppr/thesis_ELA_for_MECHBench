import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Additional quadratic term with different scaling
        f3 = 0.1 * np.sum((x_norm - 0.5)**2)
        
        # Combine terms to create a challenging landscape
        return f1 + 0.5 * f2 + f3