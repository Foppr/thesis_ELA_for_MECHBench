import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Sum of exponential terms with modified decay
        f3 = np.sum(np.exp(-2 * x_norm**2))
        
        # Additional interaction term between dimensions
        f4 = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine terms with different weights
        return 0.4 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4