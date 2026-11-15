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
        f2 = 0.2 * np.sum(np.sin(7 * np.pi * x_normalized)**5)
        f3 = 0.1 * np.sum(np.cos(5 * np.pi * x_normalized)**3)
        f4 = 0.07 * np.sum(np.sin(3 * np.pi * x_normalized)**8)
        
        # Add polynomial interaction terms for increased complexity
        f5 = 0.05 * np.sum((x_normalized**2) * np.sin(2 * np.pi * x_normalized))
        
        # Combine terms to create challenging landscape
        return f1 + f2 + f3 + f4 + f5