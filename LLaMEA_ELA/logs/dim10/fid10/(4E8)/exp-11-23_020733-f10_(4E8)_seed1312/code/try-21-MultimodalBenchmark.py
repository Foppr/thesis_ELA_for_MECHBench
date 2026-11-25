import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Spherical term creating a broad, bowl-like structure
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal terms with varying frequencies to create multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Radial basis function component adding complex curvature and local optima
        f3 = np.sum(np.exp(-0.5 * np.sum((x_norm[:, np.newaxis] - np.linspace(-1, 1, self.dim))**2, axis=0)))
        
        # Additional exponential term to create steep gradients and challenge convergence
        f4 = np.sum(np.exp(-x_norm**2) * np.sin(2 * np.pi * x_norm))
        
        # Combined function with competing forces
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4