import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Multimodal term with higher frequency components and increased complexity
        f2 = 0.2 * np.sum(np.sin(11 * np.pi * x_normalized)**8 + np.cos(5 * np.pi * x_normalized)**4)
        
        # Additional cosine interaction term with varying frequencies
        f3 = 0.1 * np.sum(np.cos(4 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Radial penalty term to create more complex landscape
        f4 = 0.05 * np.sum((x_normalized**2 + 0.1 * np.sin(10 * np.pi * x_normalized))**2)
        
        # Shifted global minimum with non-linear transformation
        f5 = 0.03 * np.sum((x_normalized - 0.25)**6 + (x_normalized + 0.2)**4)
        
        return f1 + f2 + f3 + f4 + f5