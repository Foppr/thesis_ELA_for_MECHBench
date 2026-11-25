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
        f2 = np.sum(np.sin(4 * np.pi * x_norm) ** 2 + 0.6 * np.sin(8 * np.pi * x_norm) ** 2)
        
        # Additional high-frequency sinusoidal term to increase complexity
        f3 = np.sum(np.sin(12 * np.pi * x_norm) ** 2 + 0.4 * np.sin(16 * np.pi * x_norm) ** 2)
        
        # Polynomial interaction terms with modified exponents and weights
        f4 = np.sum(1.5 * x_norm**4 + 0.3 * x_norm**6)
        
        # Product term with modified scaling to create more intricate landscape
        f5 = np.prod(0.8 * np.cos(0.4 * np.pi * x_norm) ** 2 + 0.2 * np.sin(0.8 * np.pi * x_norm) ** 2)
        
        # Additional cross-terms to increase conditioning difficulty
        f6 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(2 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]))
        
        # Combine all terms with carefully tuned weights
        return 0.6 * f1 + 0.25 * f2 + 0.07 * f3 + 0.03 * f4 - 0.04 * f5 + 0.02 * f6