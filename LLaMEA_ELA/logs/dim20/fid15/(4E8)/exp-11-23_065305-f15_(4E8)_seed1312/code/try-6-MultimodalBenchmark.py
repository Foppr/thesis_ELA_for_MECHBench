import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of sinusoidal components with different frequencies
        f1 = np.sum(np.sin(2 * np.pi * x_norm))
        
        # Quadratic penalty term
        f2 = 0.1 * np.sum(x_norm**2)
        
        # High-frequency oscillation component
        f3 = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Product of all dimensions (creates complex interactions)
        f4 = np.prod(np.sin(x_norm))
        
        # Add noise-like component with multiple local minima
        f5 = 0.01 * np.sum((x_norm - np.sin(x_norm))**2)
        
        return f1 + f2 + f3 + f4 + f5