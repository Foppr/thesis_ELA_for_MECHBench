import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.5 * np.sin(6 * np.pi * x_norm) ** 2)
        
        # Polynomial terms creating deeper local minima
        f3 = np.sum(x_norm**6 - 3 * x_norm**4 + 2 * x_norm**2)
        
        # Additional harmonic term to increase landscape complexity
        f4 = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm))
        
        # Combine all components with optimized weights
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4