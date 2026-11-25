import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Higher-order polynomial terms for increased complexity
        f1 = np.sum(x_norm**6)
        
        # Enhanced sinusoidal components with multiple frequencies and decay
        distances = np.sqrt(np.sum(x_norm**2))
        decay_factor = np.exp(-distances * 3.0)
        
        # Multiple sinusoidal frequencies with varying amplitudes
        f2 = np.sum(decay_factor * (np.sin(15 * np.pi * x_norm) + 0.5 * np.cos(8 * np.pi * x_norm)))
        
        # Adaptive coupling between dimensions based on distance from origin
        f3 = 0.3 * np.sum(x_norm[:-1] * x_norm[1:] * (1.0 + 0.5 * distances))
        
        # Additional cross-terms with trigonometric modulation
        f4 = 0.2 * np.sum(np.sin(7 * np.pi * x_norm[:-1]) * np.cos(3 * np.pi * x_norm[1:]))
        
        # Combine all components with different weights
        return f1 + f2 + f3 + f4 + 0.05 * np.sum(x_norm**8)