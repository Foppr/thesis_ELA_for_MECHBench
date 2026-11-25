import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base with conditioning
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = 0.8 * np.sum(np.sin(25 * x_normalized) ** 2)
        f3 = 0.6 * np.sum(np.cos(18 * x_normalized) ** 2)
        
        # Cross-dimensional polynomial interactions
        f4 = 0.2 * np.sum(x_normalized[:-1] * x_normalized[1:] ** 3)
        f5 = 0.15 * np.sum(x_normalized[:-2] ** 2 * x_normalized[1:-1] * x_normalized[2:] ** 4)
        
        # Radial conditioning factor that increases with dimensionality
        radius = np.sqrt(np.sum(x_normalized**2))
        radial_factor = 1.0 + 0.5 * np.exp(0.1 * self.dim) * (radius - 1.0)**2
        
        # Add a quartic term to increase curvature near boundaries
        f6 = 0.1 * np.sum((x_normalized**2 - 1.0)**2)
        
        return radial_factor * (f1 + f2 + f3 + f4 + f5 + f6)