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
        f2 = np.sum(np.sin(39 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.97 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**4) * np.sin(5.1 * np.pi * x_norm))
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(0.9 * np.abs(x_norm))) * np.cos(3.1 * np.pi * x_norm**2 + 0.22 * np.sin(7.1 * x_norm)))
        
        # New dynamic phase shift term based on dimensionality
        phase_shift = np.sum(np.sin(0.45 * np.pi * x_norm * (1 + 0.35 * self.dim)) * np.cos(0.85 * np.pi * x_norm**3))
        
        # Novel hybrid interaction term combining exponential and logarithmic scaling
        f6 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.log(np.abs(x_norm) + 1.07) * (1 + 0.65 * np.sin(self.dim * x_norm))))
        
        # Fractal-like component with recursive sine-cosine interactions
        fractal_term = np.sum(np.sin(np.pi * x_norm * np.sin(2.3 * np.pi * x_norm)) * np.cos(np.pi * x_norm * np.cos(1.7 * np.pi * x_norm)))
        
        # Adaptive scaling factor based on dimensionality and input magnitude
        scale_factor = 1.0 + 0.75 * np.log(self.dim + 1) + 0.2 * np.mean(np.abs(x_norm))
        
        # Combined function with multiple competing forces
        return scale_factor * (0.59 * f1 + 0.36 * f2 - 0.29 * f3 + 0.18 * f4 + 0.10 * f5 + 0.055 * phase_shift + 0.04 * f6 + 0.03 * fractal_term) + 0.022 * np.sum(x_norm**5)