import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical quadratic term for global structure
        f1 = np.sum(x_norm**2)
        
        # Exponential decay terms with sinusoidal modulation
        f2 = np.sum(np.exp(-0.5 * np.sum(x_norm**2)) * np.sin(2 * np.pi * x_norm))
        
        # Coupled trigonometric interactions creating complex landscape
        f3 = np.sum(np.cos(np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Product of transformed dimensions with varying scales
        f4 = np.prod(np.exp(-x_norm**2) * np.cos(x_norm))
        
        # Polynomial cross-terms with adaptive weights
        f5 = 0.1 * np.sum((x_norm**4 + 0.3 * x_norm**5))
        
        # Additional high-frequency oscillations for increased complexity
        f6 = 0.7 * np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * (self.dim - 1) / 10.0
        
        return scale_factor * (f1 + 0.6 * f2 + 0.4 * f3 + 0.3 * f4 + 0.5 * f5 + 0.8 * f6)