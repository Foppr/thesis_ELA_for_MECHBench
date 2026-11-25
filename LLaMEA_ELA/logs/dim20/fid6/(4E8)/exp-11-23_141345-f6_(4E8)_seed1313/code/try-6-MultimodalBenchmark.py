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
        f2 = 0.1 * np.sum(np.sin(5 * np.pi * x_normalized)**6)
        
        # Additional oscillatory term to increase complexity
        f3 = 0.05 * np.sum(np.cos(10 * np.pi * x_normalized) + np.sin(3 * np.pi * x_normalized))
        
        return f1 + f2 + f3