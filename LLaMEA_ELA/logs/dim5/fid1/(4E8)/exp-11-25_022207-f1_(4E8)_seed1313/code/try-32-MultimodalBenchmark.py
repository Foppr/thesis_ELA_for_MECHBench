import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Higher-order polynomial terms for increased complexity
        f1 = np.sum(x_norm**6)
        
        # Multiple sinusoidal frequencies with adaptive decay based on dimensionality
        distances = np.sqrt(np.sum(x_norm**2))
        decay_factor = np.exp(-distances * 3.0)
        
        # Multiple frequency components with different amplitudes
        f2 = np.sum(decay_factor * (np.sin(15 * np.pi * x_norm) + 0.5 * np.cos(8 * np.pi * x_norm)))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        f3 = 0.3 * np.sum(x_norm[:-1] * x_norm[1:] * (1 + 0.1 * np.abs(x_norm[:-1]) * np.abs(x_norm[1:])))
        
        # Additional oscillatory component with radial dependence
        radial_freq = 20 * distances
        f4 = 0.2 * np.sum(np.sin(radial_freq * x_norm) * np.cos(radial_freq * x_norm))
        
        # Combine all components with different weights
        return f1 + f2 + f3 + f4 + 0.05 * np.sum(x_norm**8)