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
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.7 * np.sin(6 * np.pi * x_norm) ** 2)
        
        # Additional high-frequency sinusoidal term to increase complexity
        f3 = np.sum(np.sin(10 * np.pi * x_norm) ** 2 + 0.5 * np.sin(14 * np.pi * x_norm) ** 2)
        
        # Polynomial interaction terms with modified exponents and weights
        f4 = np.sum(1.2 * x_norm**4 + 0.4 * x_norm**6 + 0.1 * x_norm**8)
        
        # Product term with modified scaling to create more intricate landscape
        f5 = np.prod(0.7 * np.cos(0.3 * np.pi * x_norm) ** 2 + 0.3 * np.sin(0.6 * np.pi * x_norm) ** 2)
        
        # Cross-term interaction to increase conditioning difficulty
        f6 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(2 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]))
        
        # Combine all terms with carefully tuned weights
        return 0.5 * f1 + 0.3 * f2 + 0.08 * f3 + 0.04 * f4 - 0.05 * f5 + 0.03 * f6