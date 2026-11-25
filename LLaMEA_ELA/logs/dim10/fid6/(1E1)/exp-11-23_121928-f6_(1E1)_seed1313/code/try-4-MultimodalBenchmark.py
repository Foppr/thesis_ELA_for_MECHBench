import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine terms with exponential scaling
        frequencies = np.exp(np.arange(self.dim) * 0.5) + 1.0
        f2 = np.sum(np.sin(frequencies * np.pi * x_norm)**2)
        
        # Cosine terms with varying amplitudes and phases
        f3 = np.sum(np.cos(2 * np.pi * x_norm * (1 + np.arange(self.dim)))**3)
        
        # Exponential penalty for large values
        f4 = np.sum(np.exp(0.5 * np.abs(x_norm)) - 1.0)
        
        # Cross-dimensional interaction term
        f5 = np.prod(np.sin(np.pi * x_norm / 4.0) + 0.5)
        
        # Combined function with complex landscape
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 - 0.05 * f5 + 0.005 * np.sum(x_norm**6)