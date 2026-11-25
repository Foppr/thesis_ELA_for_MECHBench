import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple local minima
        f2 = 0.1 * np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Product term creating complex landscape
        f3 = np.prod(np.cos(x_normalized))
        
        # Additional trigonometric interaction term to increase complexity
        f4 = 0.05 * np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combined function with multiple peaks and valleys
        return adaptive_scale * (f1 + f2 + 0.5 * f3 + 0.1 * np.sum(x_normalized**4) + f4)