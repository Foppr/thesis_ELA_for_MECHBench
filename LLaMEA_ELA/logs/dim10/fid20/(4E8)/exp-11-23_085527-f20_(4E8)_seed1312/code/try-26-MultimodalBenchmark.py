import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squared terms with different frequencies
        f1 = np.sum(x_normalized**2)
        
        # High-frequency oscillations creating many local minima
        f2 = 20 * np.sum(np.sin(10 * np.pi * x_normalized)**2)
        
        # Additional cubic terms for increased complexity
        f3 = 0.5 * np.sum(x_normalized**3)
        
        # Cross-terms creating interactions between dimensions with non-separable structure
        f4 = 0.3 * np.sum((x_normalized[:-1] + x_normalized[1:])**2)
        
        # Additional quadratic terms with different scales and shifts
        f5 = 0.1 * np.sum((x_normalized - 0.5)**2)
        
        # Mixed sine-cosine oscillations for enhanced multimodality
        f6 = 10 * np.sum(np.sin(5 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6