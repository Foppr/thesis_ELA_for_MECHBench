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
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 0.7 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**4) * np.sin(3 * np.pi * x_norm))
        
        # Enhanced chaotic interaction term using fractional exponents and adaptive modulation
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(0.3 * np.abs(x_norm)**1.5)) * 
                   np.cos(2 * np.pi * x_norm**2 + 0.1 * np.sin(5 * x_norm) * (1 + 0.2 * np.abs(x_norm))))
        
        # Gradient-based conditioning term to increase conditioning difficulty
        grad_cond = np.sum(np.abs(x_norm) * np.exp(-np.abs(x_norm)))
        
        # Adaptive sinusoidal modulation based on dimensionality
        adapt_mod = np.sum(np.sin(np.pi * x_norm * (1 + 0.1 * np.log(self.dim + 1))) * 
                          np.cos(2 * np.pi * x_norm**1.5))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combined function with multiple competing forces
        return scale_factor * (0.5 * f1 + 0.25 * f2 - 0.1 * f3 + 0.06 * f4 + 0.04 * f5 + 0.03 * grad_cond + 0.02 * adapt_mod) + 0.01 * np.sum(x_norm**5)