import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos term with mixed exponents
        f1 = np.sum((x_norm**2 + 0.3 * x_norm**4 + 0.05 * x_norm**6) ** 2)
        
        # Radial basis function component with Gaussian-like peaks
        f2 = np.sum(np.exp(-5 * np.sum((x_norm[:, np.newaxis] - np.linspace(-1, 1, self.dim))**2, axis=0)))
        
        # Spherical harmonic interaction terms for directional complexity
        f3 = np.sum(np.sin(3 * np.sum(x_norm**2)) * np.cos(2 * np.sum(x_norm**3)))
        
        # Cross-dimensional coupling with trigonometric modulation
        f4 = np.sum(np.sin(np.pi * x_norm[:-1] * x_norm[1:]) * np.cos(np.pi * x_norm[:-1] + x_norm[1:]))
        
        # Multi-scale sinusoidal interference patterns
        f5 = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * np.sin(5 * x_norm))
        
        # Chaotic modulation with varying frequency components
        f6 = np.sum(np.sin(2 * np.pi * x_norm * np.sin(3 * np.pi * x_norm)) ** 3)
        
        # Higher-order polynomial with random coefficients for added complexity
        f7 = np.sum((x_norm**3 + 0.5 * x_norm**5 + 0.1 * x_norm**7) ** 2)
        
        # Combine all components with carefully tuned weights
        return 0.5 * f1 + 0.3 * f2 + 0.25 * f3 + 0.2 * f4 + 0.15 * f5 + 0.1 * f6 + 0.05 * f7