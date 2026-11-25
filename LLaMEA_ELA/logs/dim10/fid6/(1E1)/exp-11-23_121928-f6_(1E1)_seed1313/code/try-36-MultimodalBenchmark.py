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
        f2 = np.sum(np.sin(20 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.5 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**5) * np.sin(4 * np.pi * x_norm))
        
        # Enhanced chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(0.7 * np.abs(x_norm))) * np.cos(3 * np.pi * x_norm**2 + 0.15 * np.sin(6 * x_norm)))
        
        # Modified exponential scaling factor based on dimensionality
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Combined function with multiple competing forces
        result = scale_factor * (0.5 * f1 + 0.25 * f2 - 0.12 * f3 + 0.06 * f4 + 0.04 * f5) + 0.015 * np.sum(x_norm**6)
        
        # Add a small Gaussian noise term to increase robustness
        noise = 0.001 * np.random.normal(0, 1)
        
        return result + noise