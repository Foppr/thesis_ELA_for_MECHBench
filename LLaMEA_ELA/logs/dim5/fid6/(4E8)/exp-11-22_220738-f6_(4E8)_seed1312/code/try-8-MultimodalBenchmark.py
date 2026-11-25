import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with different degrees to create varied curvature
        f1 = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric terms with multiple frequencies to introduce oscillations
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Radial basis function component to create local minima
        f3 = np.sum(np.exp(-5 * np.sum((x_norm.reshape(-1, 1) - np.linspace(-1, 1, 5))**2, axis=0)))
        
        # Cross-term interactions to increase complexity
        f4 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(np.pi * x_norm[:-1]))
        
        # Combine all components with different weights
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + 5 * np.sum(np.sin(x_norm**2))