import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic basin term
        quadratic = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal interference with multiple frequencies
        sinusoidal = np.sum(np.sin(7 * np.pi * x_normalized) + 0.5 * np.sin(13 * np.pi * x_normalized))
        
        # Adaptive penalty term that scales with dimensionality
        penalty = 0.2 * np.sum(x_normalized**6) + 0.1 * self.dim * np.sum(np.abs(x_normalized)**3)
        
        # Additional ruggedness term using a sum of cosines
        ruggedness = np.sum(np.cos(3 * np.pi * x_normalized) * np.exp(-0.5 * x_normalized**2))
        
        return quadratic + sinusoidal + penalty + ruggedness