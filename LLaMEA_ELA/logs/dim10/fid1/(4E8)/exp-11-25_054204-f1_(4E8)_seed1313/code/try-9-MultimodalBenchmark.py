import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term with varying coefficients
        f1 = np.sum((x_norm**2) * (np.arange(1, self.dim + 1) / self.dim))
        
        # High-frequency sinusoidal components with exponential scaling
        frequencies = np.exp(np.linspace(0, 3, self.dim))
        f2 = np.sum(np.sin(frequencies * x_norm)**4)
        
        # Coupled cosine terms creating intricate interference patterns
        f3 = np.sum(np.cos(x_norm[:-1] * x_norm[1:]) * np.arange(1, self.dim))
        
        # Exponential barrier term near boundaries
        f4 = np.sum(np.exp(-10 * (x_norm**2)))
        
        # Combined with adaptive weights for enhanced multimodality
        return 0.3 * f1 + 0.7 * f2 - 0.2 * f3 + 0.1 * f4 + 2.0