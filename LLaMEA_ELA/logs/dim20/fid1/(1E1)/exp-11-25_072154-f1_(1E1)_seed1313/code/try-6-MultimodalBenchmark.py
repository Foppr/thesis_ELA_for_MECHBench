import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base component
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Additional polynomial terms with higher degrees for complexity
        f3 = np.sum(x_norm**6 - 3 * x_norm**4 + 2 * x_norm**2)
        
        # Cross-terms to create correlations between dimensions
        f4 = np.sum((x_norm[:-1] - x_norm[1:]) ** 2)
        
        # Combined function with adjusted weights for better conditioning
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4