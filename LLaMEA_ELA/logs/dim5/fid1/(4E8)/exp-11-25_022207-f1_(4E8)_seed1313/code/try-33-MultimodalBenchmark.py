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
        decay_factor = np.exp(-distances * 3.0)
        
        # Multiple sinusoidal frequencies modulated by the decay factor
        f2 = np.sum(decay_factor * np.sin(15 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Interaction terms between dimensions with higher weight
        f3 = 0.8 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional higher-order polynomial terms
        f4 = 0.2 * np.sum(x_norm**6)
        
        # Add a small Gaussian noise term to increase ruggedness
        noise = 0.01 * np.random.normal(0, 1, self.dim)
        f5 = np.sum(noise * x_norm)
        
        # Combine all components with different weights
        return f1 + f2 + f3 + f4 + f5