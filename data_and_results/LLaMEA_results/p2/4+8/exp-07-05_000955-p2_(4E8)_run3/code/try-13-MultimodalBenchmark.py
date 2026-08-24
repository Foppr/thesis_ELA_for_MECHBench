import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial term with mixed degrees to create varied curvature
        f1 = np.sum(x_normalized**4 + 0.5 * x_normalized**2)
        
        # Trigonometric terms with varying frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Exponential interaction term to create steep gradients
        f3 = np.sum(np.exp(-x_normalized**2) - 1)
        
        # Cross-term interaction to increase complexity
        f4 = np.sum(x_normalized[:-1] * x_normalized[1:] if self.dim > 1 else [0])
        
        # Combine all terms with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.05 * f4