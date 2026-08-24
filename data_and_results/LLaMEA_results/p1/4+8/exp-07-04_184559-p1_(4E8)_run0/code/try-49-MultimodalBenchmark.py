import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal modulations with varying frequencies
        f2 = np.sum(np.sin(16 * np.pi * x_norm) * np.sin(32 * np.pi * x_norm))
        
        # Radial basis functions with multiple centers
        centers = np.linspace(-0.5, 0.5, 5)
        rbf = 0.0
        for center in centers:
            rbf += np.exp(-5.0 * np.sum((x_norm - center)**2))
        f3 = rbf
        
        # Cross-dimensional interaction terms with non-linear coupling
        f4 = 0.1 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]))
        
        # Additional chaotic barrier terms
        f5 = 0.5 * np.sum(np.sin(10 * x_norm)**4)
        
        # Combine all terms with different weights
        return f1 + 0.8 * f2 + 0.3 * f3 + 0.2 * f4 + 0.6 * f5