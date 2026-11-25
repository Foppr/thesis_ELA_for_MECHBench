import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple frequencies to create multiple local minima
        f2 = np.sum(np.sin(3 * np.pi * x_normalized)**2 + 0.5 * np.sin(6 * np.pi * x_normalized)**2)
        
        # Additional penalty term for large values with non-linear scaling
        f3 = 0.1 * np.sum(np.abs(x_normalized)**2.5)
        
        # Add a cosine term to introduce additional complexity and structure
        f4 = 0.05 * np.sum(np.cos(2 * np.pi * x_normalized) - 1)
        
        # Combine terms with different weights
        return f1 + 0.7 * f2 + f3 + 0.3 * f4