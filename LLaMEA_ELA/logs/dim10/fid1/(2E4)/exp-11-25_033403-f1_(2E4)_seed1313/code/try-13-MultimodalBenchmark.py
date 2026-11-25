import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal terms with different frequencies and amplitudes
        f2 = np.sum(np.sin(2 * np.pi * x_norm) ** 2)
        f3 = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        f4 = np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Radial component to create a central attraction
        radial = np.sum(x_norm**2)
        
        # Combine terms with different weights to control landscape complexity
        return 0.2 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.15 * radial