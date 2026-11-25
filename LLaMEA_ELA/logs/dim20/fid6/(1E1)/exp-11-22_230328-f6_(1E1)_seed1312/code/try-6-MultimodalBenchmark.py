import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal perturbations with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1)
        f2 = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * 0.5 * np.pi * x_norm))
        
        # Add a more complex cubic term with interaction between dimensions
        f3 = 0.05 * np.sum(x_norm**3 * np.sin(2 * np.pi * x_norm))
        
        # Introduce a Gaussian-like barrier term to create challenging landscapes
        f4 = 0.1 * np.sum(np.exp(-0.5 * (x_norm**2)) * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with different weights to control difficulty and multimodality
        return f1 + 0.5 * f2 + 0.1 * f3 + 0.2 * f4