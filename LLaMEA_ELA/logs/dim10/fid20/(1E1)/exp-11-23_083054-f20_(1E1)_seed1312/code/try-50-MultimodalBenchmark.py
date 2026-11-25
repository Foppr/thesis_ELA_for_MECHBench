import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed degrees for conditioning
        f1 = np.sum(0.5 * x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Trigonometric components with varying frequencies and amplitudes
        f2 = np.sum(0.8 * np.sin(3 * np.pi * x_norm) ** 2 + 0.5 * np.cos(5 * np.pi * x_norm) ** 2)
        
        # High-frequency oscillations to increase complexity
        f3 = np.sum(0.3 * np.sin(10 * np.pi * x_norm) ** 2 + 0.2 * np.cos(15 * np.pi * x_norm) ** 2)
        
        # Exponential interaction terms for non-separability
        f4 = np.sum(np.exp(0.5 * x_norm**2) - 1.0 + 0.1 * np.exp(2.0 * x_norm**2) - 1.0)
        
        # Cross-terms to create complex interactions between dimensions
        f5 = np.sum((x_norm[:-1] + x_norm[1:]) ** 2 + 0.5 * (x_norm[:-1] - x_norm[1:]) ** 4)
        
        # Combine all components with carefully adjusted weights
        return 0.7 * f1 + 0.15 * f2 + 0.1 * f3 + 0.03 * f4 + 0.02 * f5