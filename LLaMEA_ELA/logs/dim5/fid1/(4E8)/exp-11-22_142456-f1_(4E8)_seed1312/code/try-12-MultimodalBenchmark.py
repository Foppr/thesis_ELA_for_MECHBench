import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2)
        
        # Additional high-frequency sinusoidal component
        f3 = np.sum(np.sin(7 * np.pi * x_norm) ** 2)
        
        # Product term with exponential decay to create complex interactions
        f4 = np.prod(np.exp(-0.5 * x_norm**2))
        
        # Add a Gaussian-like peak term to increase complexity
        f5 = np.exp(-0.5 * np.sum(x_norm**2))
        
        # Combine terms with different weights to create multimodal landscape
        return 0.1 * f1 + 0.2 * f2 + 0.15 * f3 + 0.3 * f4 + 0.25 * f5 + 1.0