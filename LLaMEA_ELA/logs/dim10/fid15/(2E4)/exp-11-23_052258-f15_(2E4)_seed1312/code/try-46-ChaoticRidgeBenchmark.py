import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies
        f1 = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) + np.sin(5.0 * x) * np.cos(4.0 * x))
        
        # Polynomial chaos with mixed degrees and coefficients
        f2 = np.sum(0.5 * x**6 - 2.3 * x**4 + 3.7 * x**2 - 1.2 * x)
        
        # Radial basis function component for multimodality
        f3 = np.sum(np.exp(-0.5 * (x - 2.0)**2) + np.exp(-0.5 * (x + 2.0)**2))
        
        # Chaotic interaction terms using logistic map-like behavior
        f4 = np.sum(np.sin(10.0 * np.abs(x)) * np.cos(7.0 * x) * np.exp(-0.1 * x**2))
        
        # High-frequency oscillations for increased complexity
        f5 = 0.3 * np.sum(np.sin(20.0 * x) + np.cos(15.0 * x) + np.sin(25.0 * x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5