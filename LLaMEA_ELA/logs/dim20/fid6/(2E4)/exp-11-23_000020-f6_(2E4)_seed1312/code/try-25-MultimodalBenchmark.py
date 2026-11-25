import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**2 + np.sin(7 * np.pi * x_norm)**2)
        
        # Product term creating complex landscape with multiple peaks
        f3 = np.prod(np.cos(0.8 * np.pi * x_norm) + 0.5)
        
        # Higher-order polynomial interaction terms
        f4 = np.sum(x_norm**4 + 0.5 * x_norm**3)
        
        # Shifted global minimum term with non-linear transformation
        f5 = np.sum((x_norm + 0.3)**4)
        
        # Additional cross-term interaction creating intricate landscape
        f6 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with varying weights
        return 0.1 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + 0.1 * f5 + 0.1 * f6 + 2.0