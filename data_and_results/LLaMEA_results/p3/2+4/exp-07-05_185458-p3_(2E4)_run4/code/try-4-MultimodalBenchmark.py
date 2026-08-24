import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base function
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        f2 = np.sum(np.sin(10 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm) ** 2)
        
        # Polynomial coupling between dimensions
        f3 = np.sum((x_norm[:-1] + x_norm[1:]) ** 4)
        
        # Adaptive difficulty term based on dimensionality
        f4 = np.sum(np.sin(20 * np.pi * x_norm) ** 4) * (1 + 0.1 * self.dim)
        
        # Combine all terms with carefully chosen weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4