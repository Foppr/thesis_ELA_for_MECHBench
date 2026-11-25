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
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies
        f3 = np.prod(np.cos(5 * x_norm))
        
        # Polynomial interaction term between adjacent dimensions
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Modified Rosenbrock-like term for additional challenge
        f5 = np.sum((x_norm[:-1]**2 - x_norm[1:])**2)
        
        # Additional harmonic interaction with nested trigonometric terms
        f6 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Nested trigonometric composition for increased complexity
        f7 = np.sum(np.sin(np.cos(4 * np.pi * x_norm))**2)
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine terms with adaptive weights
        result = (0.3 * f1 + 
                 0.9 * f2 + 
                 0.4 * f3 + 
                 0.5 * f4 + 
                 0.7 * f5 + 
                 0.3 * f6 + 
                 0.2 * f7) * scale_factor
        
        # Add small noise for additional challenge
        noise = 0.005 * np.random.random()
        
        return result + noise