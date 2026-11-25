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
        f2 = np.sum(np.sin(9 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies
        f3 = np.prod(np.cos(5 * x_norm))
        
        # Polynomial interaction term between adjacent dimensions
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Modified Rosenbrock-like term for additional challenge
        f5 = np.sum((x_norm[:-1]**2 - x_norm[1:])**2)
        
        # Additional harmonic interaction with cubic terms
        f6 = np.sum(x_norm**3 * np.sin(4 * np.pi * x_norm))
        
        # Higher-order polynomial interaction
        f7 = np.sum((x_norm[:-1] ** 4 - x_norm[1:] ** 4) ** 2)
        
        # Asymmetric frequency shifts to increase complexity
        f8 = np.sum(np.sin(6 * np.pi * x_norm + 0.5 * x_norm**2)**2)
        
        # Cross-term interactions with exponential decay
        f9 = np.sum(np.exp(-x_norm**2) * np.cos(8 * x_norm))
        
        # Add small noise for additional challenge
        noise = 0.01 * np.random.random()
        
        return 0.5 * f1 + 0.8 * f2 + 0.3 * f3 + 0.6 * f4 + 0.7 * f5 + 0.4 * f6 + 0.4 * f7 + 0.5 * f8 + 0.3 * f9 + noise