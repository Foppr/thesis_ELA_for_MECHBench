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
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Sum of exponential terms
        f3 = np.sum(np.exp(-x_norm**2))
        
        # Combine terms with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3