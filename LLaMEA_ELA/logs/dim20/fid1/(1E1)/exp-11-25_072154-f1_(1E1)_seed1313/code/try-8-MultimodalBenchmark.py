import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Additional sinusoidal terms with different frequencies and amplitudes
        f3 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.5 * np.sin(7 * np.pi * x_norm) ** 2)
        
        # Polynomial terms to create complex curvature and plateaus
        f4 = np.sum(x_norm**6 - 3 * x_norm**4 + 2 * x_norm**2)
        
        # Cross-terms to increase dimensionality interaction
        f5 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(5 * np.pi * x_norm[:-1]))
        
        # Combine all components with optimized weights for better discrimination
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.05 * f4 + 0.05 * f5