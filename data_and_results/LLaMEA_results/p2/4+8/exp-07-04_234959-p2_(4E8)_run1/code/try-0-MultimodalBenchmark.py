import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Add a small noise term to make it more challenging
        noise = 0.1 * np.random.random()
        
        return f1 + 0.1 * f2 + noise