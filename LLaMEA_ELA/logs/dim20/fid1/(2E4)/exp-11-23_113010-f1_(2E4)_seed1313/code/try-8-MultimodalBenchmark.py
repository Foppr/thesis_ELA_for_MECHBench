import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        term1 = np.sum(x_norm**2)
        
        # Sum of sine terms with different frequencies
        term2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Product of cosines for additional complexity
        term3 = np.prod(np.cos(3 * np.pi * x_norm))
        
        # Additional interaction term between all dimensions
        term4 = np.sum(x_norm**4) * 0.1
        
        # Add a small noise component to create more complex landscape
        noise = 0.05 * np.random.random()
        
        return term1 + 0.7 * term2 - 0.4 * term3 + term4 + noise