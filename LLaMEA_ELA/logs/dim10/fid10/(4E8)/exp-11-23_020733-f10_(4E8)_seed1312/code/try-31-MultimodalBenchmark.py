import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial term with mixed degrees to create valleys and ridges
        f1 = np.sum(x_norm**6 + 0.3 * x_norm**4 + 0.1 * x_norm**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) + 
                   0.5 * np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm))
        
        # Enhanced exponential barrier with sharper gradients near boundaries
        f3 = np.sum(np.exp(-x_norm**2) - 1 + 0.2 * np.exp(-x_norm**2 / 0.5))
        
        # Additional quadratic interaction term to create more complex landscape
        f4 = 0.1 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Combined function with competing forces
        return 0.4 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4