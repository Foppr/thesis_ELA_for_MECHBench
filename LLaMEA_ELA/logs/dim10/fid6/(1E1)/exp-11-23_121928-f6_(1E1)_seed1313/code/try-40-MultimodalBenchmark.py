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
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(0.5 * np.abs(x_norm))) * np.cos(2 * np.pi * x_norm**2 + 0.1 * np.sin(5 * x_norm)))
        
        # Enhanced chaotic term with Gaussian modulation
        gaussian_noise = np.random.normal(0, 0.1, self.dim)
        f6 = np.sum(np.sin(np.pi * x_norm * np.exp(0.3 * np.abs(x_norm))) * 
                   np.cos(3 * np.pi * x_norm**2 + 0.2 * np.sin(7 * x_norm) + gaussian_noise))
        
        # Higher-order polynomial scaling for dynamic difficulty
        f7 = np.sum(x_norm**6 * np.cos(2 * np.pi * x_norm))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combined function with multiple competing forces
        return scale_factor * (0.5 * f1 + 0.25 * f2 - 0.1 * f3 + 0.07 * f4 + 0.02 * f5 + 0.03 * f6 + 0.01 * f7) + 0.01 * np.sum(x_norm**5)