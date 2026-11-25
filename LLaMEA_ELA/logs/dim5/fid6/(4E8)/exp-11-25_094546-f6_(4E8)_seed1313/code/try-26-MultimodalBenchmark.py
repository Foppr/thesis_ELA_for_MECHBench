import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with higher frequency sinusoidal components
        f2 = 0.2 * np.sum(np.cos(10 * np.pi * x_norm) + 0.5 * np.cos(20 * np.pi * x_norm))
        
        # Additional penalty for large values with quartic and quintic terms
        f3 = 0.02 * np.sum(x_norm**4 + 0.1 * x_norm**5)
        
        # Add a composite multimodal term with different frequencies
        f4 = 0.15 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        return f1 + f2 + f3 + f4