import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies and added cross-terms
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2) + 0.5 * np.sum(np.sin(3 * np.pi * x_norm)**2)
        
        # Sum of exponential terms with additional interaction
        f3 = np.sum(np.exp(-x_norm**2)) + 0.3 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine terms with different weights
        return 0.4 * f1 + 0.3 * f2 + 0.3 * f3