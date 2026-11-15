import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal terms with varying frequencies to create multiple local minima
        sinusoidal = np.sum(np.sin(7 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized))
        
        # Cross-dimensional interaction terms using exponential decay
        cross_dim = np.sum(np.exp(-np.sum((x_normalized[:, np.newaxis] - x_normalized[np.newaxis, :])**2, axis=1) / (2 * 0.5**2)))
        
        # Product term with higher frequency to create more complex landscape
        product = np.prod(np.cos(3 * np.pi * x_normalized))
        
        # Combine terms with different weights to create a challenging landscape
        return quadratic + 0.15 * sinusoidal + 0.08 * cross_dim + 0.03 * product