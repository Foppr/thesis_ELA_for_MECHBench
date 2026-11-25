import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Periodic oscillation with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Saddle point inducing term with exponential decay
        f3 = 0.2 * np.sum(np.exp(-x_norm**2) * np.sin(2 * np.pi * x_norm))
        
        # Conditional interaction term that activates based on dimension parity
        f4 = 0.1 * np.sum((x_norm[:-1] * x_norm[1:]) * (1 + 0.5 * np.sin(np.pi * x_norm[:-1])))
        
        # Fourth-order polynomial for increased curvature
        f5 = 0.05 * np.sum(x_norm**4)
        
        # Cross-dimensional interaction with non-linear scaling
        f6 = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) ** 1.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6