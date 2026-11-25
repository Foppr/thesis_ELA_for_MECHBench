import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine terms creating many local minima
        f2 = np.sum(np.sin(11 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies
        f3 = np.prod(np.cos(5 * x_norm))
        
        # Polynomial interaction term between adjacent dimensions
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Modified Rosenbrock-like term for additional challenge
        f5 = np.sum((x_norm[:-1]**2 - x_norm[1:])**2)
        
        # Additional harmonic interaction with cubic terms
        f6 = np.sum(x_norm**3 * np.sin(5 * np.pi * x_norm))
        
        # Cubic polynomial interaction
        f7 = np.sum((x_norm[:-1] ** 3 - x_norm[1:] ** 3) ** 2)
        
        # Multi-scale trigonometric coupling with asymmetric frequencies
        f8 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Cross-dimensional polynomial coupling
        f9 = np.sum((x_norm**4 + x_norm**2 - 1)**2)
        
        # Asymmetric frequency shifts for additional complexity
        f10 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Higher-order polynomial interactions
        f11 = np.sum((x_norm[:-2] - x_norm[1:-1] + x_norm[2:])**3)
        
        # Add small noise for additional challenge
        noise = 0.01 * np.random.random()
        
        return 0.5 * f1 + 1.2 * f2 + 0.6 * f3 + 0.4 * f4 + 0.8 * f5 + 0.4 * f6 + 0.3 * f7 + 0.7 * f8 + 0.5 * f9 + 0.6 * f10 + 0.4 * f11 + noise