import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with exponential scaling
        f2 = np.sum(np.exp(2 * np.abs(x_normalized)) * np.sin(10 * np.pi * x_normalized))
        
        # Polynomial barrier terms creating sharp local minima
        f3 = np.sum((x_normalized**4 - 0.5 * x_normalized**2 + 0.1)**2)
        
        # Product of transformed variables creating complex interaction
        f4 = np.prod(np.cos(3 * x_normalized) + 0.5 * np.sin(7 * x_normalized))
        
        # Additional high-order polynomial for increased curvature
        f5 = 0.3 * np.sum(x_normalized**6)
        
        # Combined function with multiple conflicting objectives
        return f1 + f2 + f3 + 0.5 * f4 + f5 + 0.05 * np.sum(np.abs(x_normalized)**3)