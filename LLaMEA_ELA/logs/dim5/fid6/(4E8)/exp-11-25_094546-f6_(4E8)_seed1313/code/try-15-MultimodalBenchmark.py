import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        f1 = np.sum(x_norm**2)
        
        # Highly multimodal term with exponentially increasing frequencies
        f2 = 0.05 * np.sum(np.cos(np.pi * np.power(2, np.arange(1, self.dim + 1)) * x_norm))
        
        # Additional polynomial conditioning with varying exponents
        f3 = 0.02 * np.sum(np.abs(x_norm)**(3 + np.arange(self.dim)))
        
        # Adaptive penalty based on distance from origin
        dist = np.sqrt(np.sum(x_norm**2))
        f4 = 0.1 * dist * np.sin(10 * dist)
        
        return f1 + f2 + f3 + f4