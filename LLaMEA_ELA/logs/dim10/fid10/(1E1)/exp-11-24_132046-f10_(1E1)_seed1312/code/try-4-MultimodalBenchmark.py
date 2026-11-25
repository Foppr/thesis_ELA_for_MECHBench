import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal oscillations with varying frequencies
        f2 = 0.2 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Additional high-frequency component to increase complexity
        f3 = 0.15 * np.sum(np.sin(11 * np.pi * x_norm**2))
        
        # Fourth-order polynomial term for additional curvature
        f4 = 0.02 * np.sum(x_norm**4)
        
        # Cross-terms to create interaction between dimensions
        f5 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + f2 + f3 + f4 + f5