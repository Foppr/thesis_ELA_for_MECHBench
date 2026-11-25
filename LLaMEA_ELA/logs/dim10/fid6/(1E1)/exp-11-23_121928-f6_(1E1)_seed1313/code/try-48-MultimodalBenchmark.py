import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine terms creating many local minima
        f2 = np.sum(np.sin(17 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.8 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**4) * np.sin(3.5 * np.pi * x_norm))
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(0.6 * np.abs(x_norm))) * np.cos(2.1 * np.pi * x_norm**2 + 0.12 * np.sin(5.2 * x_norm)))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.6 * np.log(self.dim + 1)
        
        # Combined function with multiple competing forces
        return scale_factor * (0.55 * f1 + 0.35 * f2 - 0.18 * f3 + 0.09 * f4 + 0.04 * f5) + 0.015 * np.sum(x_norm**5)