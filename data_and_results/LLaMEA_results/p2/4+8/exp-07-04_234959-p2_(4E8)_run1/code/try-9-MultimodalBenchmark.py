import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima and increased frequency
        f2 = np.sum(np.sin(7 * np.pi * x_norm) ** 2)
        
        # Add a small noise term to make it more challenging
        noise = 0.05 * np.random.random()
        
        # Shift the global minimum to (0.5, 0.5, ..., 0.5)
        shift = np.full(self.dim, 0.5)
        f3 = np.sum((x_norm - shift)**2)
        
        return f1 + 0.15 * f2 + 0.05 * f3 + noise