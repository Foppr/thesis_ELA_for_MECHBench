import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2) + 0.5 * np.sum(np.sin(7 * np.pi * x_norm) ** 2)
        
        # Additional high-frequency oscillation to increase complexity
        f3 = np.sum(np.sin(11 * np.pi * x_norm) ** 2)
        
        # Combined polynomial penalty with mixed powers
        f4 = 0.1 * np.sum(x_norm**6) + 0.05 * np.sum(np.abs(x_norm)**3)
        
        # Cross-term interaction to create more complex landscape
        f5 = 0.01 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2)
        
        return f1 + 0.2 * f2 + 0.1 * f3 + 0.02 * f4 + 0.005 * f5