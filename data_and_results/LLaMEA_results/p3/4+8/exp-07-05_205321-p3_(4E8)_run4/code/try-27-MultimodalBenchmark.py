import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial terms to create complex interactions
        polynomial = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Trigonometric terms with varying frequencies to create multiple local minima
        trigonometric = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Exponential decay term to create a complex landscape
        exponential = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(4 * np.pi * x_norm))
        
        # Cross-term interaction to increase dimensionality complexity
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(np.pi * x_norm[:-1]))
        
        # Combine all terms with different weights
        return 0.2 * polynomial + 0.3 * trigonometric + 0.3 * exponential + 0.2 * cross_term + 1.0