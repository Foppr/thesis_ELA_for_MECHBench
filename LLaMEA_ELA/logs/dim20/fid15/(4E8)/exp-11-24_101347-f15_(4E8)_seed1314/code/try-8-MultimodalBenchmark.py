import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squared terms with exponential scaling
        term1 = np.sum(np.exp(0.5 * x_normalized**2))
        
        # Product of cosines creating multiple local minima with varying frequencies
        term2 = np.prod(np.cos(2.0 * x_normalized) * np.sin(1.5 * x_normalized))
        
        # Additional high-frequency sinusoidal component for complexity
        term3 = np.sum(np.sin(10.0 * x_normalized**3))
        
        # Exponential barrier terms to create saddle points
        term4 = np.sum(np.exp(-x_normalized**2) * np.cos(5.0 * x_normalized))
        
        # Combine all terms with different weights and add a constant offset
        result = 15 * term1 + 8 * term2 + 3 * term3 + 5 * term4 + 10
        
        return result