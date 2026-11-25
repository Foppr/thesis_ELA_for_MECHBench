import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Additional cosine terms with varying frequencies
        f3 = np.sum(np.cos(7 * np.pi * x_norm) ** 2)
        
        # Exponential penalty for large values to create steep gradients
        f4 = np.sum(np.exp(0.5 * np.abs(x_norm)) - 1)
        
        # Polynomial cross-terms to introduce coupling between dimensions
        f5 = np.sum((x_norm**4 + 0.1 * x_norm**3 + 0.01 * x_norm**2) / (1 + np.abs(x_norm)))
        
        # Combine all terms with carefully tuned weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5