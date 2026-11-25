import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term with varying weights for each dimension
        f1 = np.sum(x_norm**2)
        
        # Add multiple sinusoidal oscillations with different frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(16 * np.pi * x_norm**4) + 0.5 * np.sin(8 * np.pi * x_norm**3) + 0.3 * np.sin(4 * np.pi * x_norm**2))
        
        # Add cubic and quartic terms to create sharper gradients and more complex valleys
        f3 = 0.1 * np.sum(x_norm**3 + 0.2 * x_norm**4)
        
        # Add a chaotic component using a logistic map-like function for increased complexity
        chaos = 0.05 * np.sum(np.sin(np.pi * x_norm * np.exp(np.abs(x_norm))))
        
        # Combine all terms with different weights
        result = f1 + f2 + f3 + chaos
        
        return result