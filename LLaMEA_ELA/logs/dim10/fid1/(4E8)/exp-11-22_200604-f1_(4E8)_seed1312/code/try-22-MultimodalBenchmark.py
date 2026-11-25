import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with slight bias
        f1 = np.sum(x_norm**2) * 0.8
        
        # High-frequency sinusoidal terms with exponential scaling
        f2 = 0.3 * np.sum(np.exp(3 * np.abs(x_norm)) * np.sin(11 * np.pi * x_norm))
        
        # Quartic penalty with varying coefficients per dimension
        f3 = 0.05 * np.sum((x_norm**4) * (1 + 0.5 * np.sin(5 * np.pi * x_norm)))
        
        # Cubic term with cross-dimension interactions
        f4 = 0.1 * np.sum(x_norm**3)
        
        # Add interaction terms between dimensions to increase complexity
        interaction = 0.03 * np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(2 * x_norm[:-1] - x_norm[1:]))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + interaction
        
        return result