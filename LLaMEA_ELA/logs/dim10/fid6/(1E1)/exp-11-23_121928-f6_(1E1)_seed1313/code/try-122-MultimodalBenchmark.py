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
        f2 = np.sum(np.sin(41 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.99 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**5) * np.sin(5.3 * np.pi * x_norm))
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(1.0 * np.abs(x_norm))) * np.cos(3.3 * np.pi * x_norm**2 + 0.25 * np.sin(7.3 * x_norm)))
        
        # New dynamic phase shift term based on dimensionality
        phase_shift = np.sum(np.sin(0.47 * np.pi * x_norm * (1 + 0.37 * self.dim)) * np.cos(0.87 * np.pi * x_norm**3))
        
        # Novel hybrid interaction term combining exponential and logarithmic scaling
        f6 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.log(np.abs(x_norm) + 1.09) * (1 + 0.67 * np.sin(self.dim * x_norm))))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.8 * np.log(self.dim + 1)
        
        # Combined function with multiple competing forces
        return scale_factor * (0.61 * f1 + 0.38 * f2 - 0.31 * f3 + 0.19 * f4 + 0.11 * f5 + 0.057 * phase_shift + 0.042 * f6) + 0.024 * np.sum(x_norm**6)