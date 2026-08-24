import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base function
        f1 = np.sum(x_norm**2)
        
        # Chaotic cosine wave components with higher frequency modulation
        f2 = np.sum(np.cos(15 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) ** 3)
        
        # Polynomial coupling between dimensions
        f3 = np.sum((x_norm[:-1] + x_norm[1:]) ** 4)
        
        # Cross-term interaction between dimensions
        f4 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(10 * np.pi * x_norm[:-1]) ** 2)
        
        # Adaptive difficulty term based on dimensionality
        f5 = np.sum(np.cos(25 * np.pi * x_norm) ** 4) * (1 + 0.15 * self.dim)
        
        # Combine all terms with carefully chosen weights
        return 0.4 * f1 + 0.25 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5