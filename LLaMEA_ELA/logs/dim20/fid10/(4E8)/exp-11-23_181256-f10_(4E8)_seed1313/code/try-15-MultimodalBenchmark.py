import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal components with exponential scaling
        f2 = np.sum(np.sin(10 * np.pi * x_normalized) * np.exp(-x_normalized**2))
        
        # Polynomial barrier terms creating narrow valleys
        f3 = np.sum((x_normalized**4 + 0.1 * x_normalized**2 + 0.01)**(-1))
        
        # Cross-dimensional coupling with exponential decay
        f4 = np.exp(-np.sum(x_normalized**2) / (2 * self.dim)) * np.sin(np.sum(x_normalized**3))
        
        # Additional ruggedness through product of scaled sinusoids
        f5 = np.prod(np.sin(3 * np.pi * x_normalized) + 0.5 * np.cos(7 * np.pi * x_normalized))
        
        # Combined function with enhanced multimodality and conditioning
        return 2.0 * f1 + 0.5 * f2 + 0.3 * f3 + 0.1 * f4 + 0.2 * f5 + 0.05 * np.sum(x_normalized**6)