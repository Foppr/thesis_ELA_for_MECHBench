import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency chaotic sine terms creating many local minima
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**3)
        
        # Cosine product with varying frequencies and dynamic scaling for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.7 * np.abs(x_norm)) * np.exp(-0.1 * np.abs(x_norm))))
        
        # Additional polynomial term with exponential modulation for shaping the landscape
        f4 = np.sum((x_norm**4) * np.sin(3 * np.pi * x_norm) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Cross-term interaction creating ridges and valleys
        f5 = np.sum(np.sin(5 * x_norm) * np.cos(2 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Combined function with multiple competing forces and chaotic behavior
        return 0.4 * f1 + 0.3 * f2 - 0.15 * f3 + 0.08 * f4 + 0.07 * f5 + 0.02 * np.sum(x_norm**5)