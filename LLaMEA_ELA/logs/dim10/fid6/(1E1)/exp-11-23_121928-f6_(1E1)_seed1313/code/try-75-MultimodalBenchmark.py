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
        f2 = np.sum(np.sin(30 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.8 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**4) * np.sin(4.2 * np.pi * x_norm))
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(0.7 * np.abs(x_norm))) * np.cos(2.5 * np.pi * x_norm**2 + 0.15 * np.sin(6.0 * x_norm)))
        
        # New dynamic phase shift term based on dimensionality
        phase_shift = np.sum(np.sin(0.35 * np.pi * x_norm * (1 + 0.25 * self.dim)) * np.cos(0.75 * np.pi * x_norm**3))
        
        # Novel hybrid interaction term combining exponential and logarithmic scaling
        f6 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.log(np.abs(x_norm) + 1) * (1 + 0.55 * np.sin(self.dim * x_norm))))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.65 * np.log(self.dim + 1)
        
        # Combined function with multiple competing forces
        return scale_factor * (0.6 * f1 + 0.3 * f2 - 0.22 * f3 + 0.12 * f4 + 0.06 * f5 + 0.04 * phase_shift + 0.03 * f6) + 0.015 * np.sum(x_norm**5)