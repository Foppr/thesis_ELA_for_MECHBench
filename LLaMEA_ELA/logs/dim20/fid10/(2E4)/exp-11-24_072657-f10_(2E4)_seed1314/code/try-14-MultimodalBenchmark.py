import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term with adaptive scaling
        f1 = np.sum(x_norm**2)
        
        # Nested sine terms with varying frequencies and amplitudes
        f2 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm)**2)
        
        # Product of transformed dimensions creating complex interactions
        f3 = np.prod(np.sin(x_norm * np.pi / 2))
        
        # Higher-order polynomial with cross-terms for increased complexity
        f4 = 0.1 * np.sum((x_norm**3 + 0.5 * x_norm**4))
        
        # Additional coupled sine terms to create more local minima
        f5 = 0.5 * np.sum(np.sin(9 * np.pi * x_norm)**2)
        
        # Adaptive noise component based on dimensionality
        noise = 0.01 * (self.dim / 10.0) * np.random.random()
        
        return f1 + 0.8 * f2 + 0.3 * f3 + 0.4 * f4 + 0.6 * f5 + noise