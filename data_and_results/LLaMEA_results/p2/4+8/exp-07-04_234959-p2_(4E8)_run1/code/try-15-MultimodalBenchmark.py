import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Multimodal term with multiple local minima using different frequencies
        f2 = 0.15 * np.sum(np.sin(7 * np.pi * x_normalized)**6)
        
        # Additional cosine interaction term to create more complex landscape
        f3 = 0.05 * np.sum(np.cos(3 * np.pi * x_normalized) * np.sin(2 * np.pi * x_normalized))
        
        # Shifted global minimum to increase difficulty
        f4 = 0.02 * np.sum((x_normalized - 0.3)**4)
        
        return f1 + f2 + f3 + f4