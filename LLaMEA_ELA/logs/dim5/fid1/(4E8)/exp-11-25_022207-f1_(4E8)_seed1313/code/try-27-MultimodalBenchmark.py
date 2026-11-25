import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x_norm**4)
        
        # Sinusoidal components with exponential decay based on distance from origin
        distances = np.sqrt(np.sum(x_norm**2))
        decay_factor = np.exp(-distances * 2.0)
        
        # Multiple sinusoidal frequencies modulated by the decay factor
        f2 = np.sum(decay_factor * np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Interaction terms between dimensions
        f3 = 0.5 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all components with different weights
        return f1 + f2 + f3 + 0.1 * np.sum(x_norm**6)