import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic basin term with varying coefficients
        f1 = np.sum(0.1 * x_norm**2 + 0.9 * x_norm**4)
        
        # Coupled sinusoidal terms creating complex landscape
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Additional high-frequency oscillation for increased complexity
        f3 = np.sum(np.sin(10 * np.pi * x_norm**2) ** 2)
        
        # Product term with non-linear transformation
        f4 = np.prod(np.sin(0.5 * np.pi * x_norm**3))
        
        # Combine all terms with adaptive weights
        return 0.2 * f1 + 0.3 * f2 + 0.3 * f3 + 0.2 * f4