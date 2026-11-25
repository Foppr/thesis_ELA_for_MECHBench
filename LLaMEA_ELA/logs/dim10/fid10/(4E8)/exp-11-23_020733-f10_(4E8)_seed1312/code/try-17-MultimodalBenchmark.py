import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial term with mixed degrees to create valleys and ridges
        f1 = np.sum(x_norm**4 + 0.5 * x_norm**2)
        
        # Trigonometric terms creating multiple local minima
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential barrier term to create steep gradients near boundaries
        f3 = np.sum(np.exp(-x_norm**2 / 2) - 1)
        
        # Combined function with competing forces
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3