import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Multimodal terms with multiple local minima
        f2 = 0.15 * np.sum(np.sin(7 * np.pi * x_normalized)**8)
        
        # Additional oscillatory term to increase complexity
        f3 = 0.08 * np.sum(np.cos(12 * np.pi * x_normalized) + np.sin(4 * np.pi * x_normalized))
        
        # Higher-order polynomial interaction terms
        f4 = 0.05 * np.sum((x_normalized**4) * np.sin(2 * np.pi * x_normalized))
        
        return f1 + f2 + f3 + f4