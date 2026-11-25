import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product term that creates complex interactions
        f3 = np.prod(np.cos(x_norm))
        
        # Additional high-frequency oscillation to increase complexity
        f4 = np.sum(np.sin(10 * np.pi * x_norm**2)**2)
        
        # Cross-terms to encourage interaction between dimensions
        f5 = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combined function with multiple local minima and varied difficulty
        return f1 + 0.1 * f2 + 0.01 * f3 + 0.05 * f4 + 0.02 * f5 + 1e-6 * np.sum(x_norm**4)