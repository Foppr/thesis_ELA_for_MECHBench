import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Highly multimodal terms with multiple local minima
        f2 = 0.3 * np.sum(np.sin(10 * np.pi * x_normalized)**4 + 
                         np.cos(8 * np.pi * x_normalized)**4)
        
        # Additional complex oscillatory term with periodic global minima
        f3 = 0.1 * np.sum(np.sin(15 * np.pi * x_normalized) * 
                         np.cos(12 * np.pi * x_normalized) + 
                         np.sin(7 * np.pi * x_normalized)**3)
        
        # Add a periodic pattern that creates multiple global minima
        f4 = 0.2 * np.sum(np.cos(6 * np.pi * x_normalized) + 
                         np.sin(9 * np.pi * x_normalized))**2
        
        return f1 + f2 + f3 + f4