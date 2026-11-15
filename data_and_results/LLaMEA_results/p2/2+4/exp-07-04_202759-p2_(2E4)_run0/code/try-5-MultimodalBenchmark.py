import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal terms with varying frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential decay term to create ruggedness
        f3 = np.sum(np.exp(-x_norm**2) * np.sin(4 * np.pi * x_norm)**2)
        
        # Cross-term interaction creating complex valleys
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**2 * np.sin(5 * np.pi * x_norm[:-1])**2)
        
        # Combine terms with different weights to increase challenge
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4