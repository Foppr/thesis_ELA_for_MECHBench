import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic term for central attraction
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms to create many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Polynomial terms with different degrees to add complexity
        f3 = np.sum(x_norm**4 + 0.5 * x_norm**6)
        
        # Exponential decay with cosine modulation for additional structure
        f4 = np.sum(np.exp(-x_norm**2) * np.cos(3 * np.pi * x_norm))
        
        # Additional sinusoidal term with varying phase to increase multimodality
        f5 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Combine all terms with carefully chosen weights
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5 + 8 * np.sum(np.sin(x_norm)) + 3 * np.sum(np.cos(x_norm))