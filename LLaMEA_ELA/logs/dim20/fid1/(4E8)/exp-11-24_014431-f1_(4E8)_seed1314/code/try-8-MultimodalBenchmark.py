import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f1 = np.sum(x**2)
        
        # Exponentially increasing sinusoidal perturbations for high multimodality
        f2 = 0.5 * np.sum(np.sin(10.0 * np.exp(0.5 * np.arange(self.dim)) * x))
        
        # Cubic term with varying coefficients
        f3 = 0.05 * np.sum(x**3 * np.sin(2.0 * x))
        
        # Additional high-frequency oscillation
        f4 = 0.1 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Combine all terms with different weights
        result = f1 + f2 + f3 + f4
        
        return result