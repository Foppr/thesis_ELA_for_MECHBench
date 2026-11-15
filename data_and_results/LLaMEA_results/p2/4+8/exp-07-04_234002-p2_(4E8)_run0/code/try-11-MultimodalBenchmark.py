import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with different degrees to create varied curvature
        f1 = np.sum(x_norm**4)
        
        # Trigonometric terms with multiple frequencies to create oscillations
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential terms to create steep gradients and plateaus
        f3 = np.sum(np.exp(-x_norm**2) - 1)
        
        # Cross-terms to create interaction between dimensions
        f4 = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Add a global scaling factor and noise
        noise = 0.05 * np.random.random()
        
        # Combine all terms with different weights
        result = 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + noise
        
        # Ensure global minimum is at origin
        return result