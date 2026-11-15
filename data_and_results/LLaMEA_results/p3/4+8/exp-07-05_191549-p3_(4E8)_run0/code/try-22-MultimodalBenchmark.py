import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Enhanced multimodal terms with multiple local minima
        f2 = 0.2 * np.sum(np.sin(8 * np.pi * x_normalized)**7)
        f3 = 0.15 * np.sum(np.cos(6 * np.pi * x_normalized)**5)
        f4 = 0.1 * np.sum(np.sin(4 * np.pi * x_normalized)**9)
        f5 = 0.08 * np.sum(np.cos(2 * np.pi * x_normalized)**4)
        
        # Additional interaction terms to increase conditioning
        f6 = 0.05 * np.sum(x_normalized**4)
        f7 = 0.03 * np.sum(x_normalized**6)
        
        # Combine all terms to create challenging landscape
        return f1 + f2 + f3 + f4 + f5 + f6 + f7