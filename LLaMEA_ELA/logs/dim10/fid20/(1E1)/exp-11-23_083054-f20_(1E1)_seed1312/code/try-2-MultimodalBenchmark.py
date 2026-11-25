import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.5 * np.sin(7 * np.pi * x_norm) ** 2)
        
        # Additional high-frequency sinusoidal term to increase complexity
        f3 = np.sum(np.sin(11 * np.pi * x_norm) ** 2)
        
        # Product term with modified scaling to create more intricate landscape
        f4 = np.prod(np.cos(0.3 * np.pi * x_norm) ** 2)
        
        # Combine all terms with carefully tuned weights
        return 0.8 * f1 + 0.15 * f2 + 0.05 * f3 - 0.03 * f4