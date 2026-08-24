import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Additional multimodal terms with multiple local minima
        f2 = 0.15 * np.sum(np.sin(6 * np.pi * x_normalized)**5)
        f3 = 0.08 * np.sum(np.cos(4 * np.pi * x_normalized)**3)
        
        # Add interaction terms between dimensions for increased complexity
        f4 = 0.05 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Combine all terms to create challenging landscape
        return f1 + f2 + f3 + f4