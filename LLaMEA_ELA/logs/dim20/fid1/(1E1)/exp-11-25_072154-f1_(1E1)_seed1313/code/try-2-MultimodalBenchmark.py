import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with varying wavelengths
        f2 = np.sum(np.sin(10 * np.pi * x_norm) ** 2 + 0.5 * np.sin(20 * np.pi * x_norm) ** 2)
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        f3 = np.sum((r + 0.5 * np.sin(15 * r))**2)
        
        # Polynomial terms with mixed exponents
        f4 = np.sum(x_norm**6 - 3 * x_norm**4 + 2 * x_norm**2)
        
        # Cross-terms creating complex interaction
        f5 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(5 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Combine all components with different weights
        return 0.3 * f1 + 0.4 * f2 + 0.15 * f3 + 0.1 * f4 + 0.05 * f5