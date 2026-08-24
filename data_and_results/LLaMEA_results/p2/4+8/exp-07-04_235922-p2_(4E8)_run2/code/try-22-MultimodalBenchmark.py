import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add quadratic and exponential decay terms
        for i in range(self.dim):
            result += (x[i] ** 2) * np.exp(-0.1 * abs(x[i]))
        
        # Add trigonometric interference patterns
        for i in range(self.dim):
            result += 0.5 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Add interaction terms between variables
        for i in range(self.dim - 1):
            result += 0.3 * np.sin(x[i] * x[i + 1]) * np.exp(-0.05 * (x[i] ** 2 + x[i + 1] ** 2))
        
        # Add a chaotic component using a logistic map-like term
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10 * x[i]) * np.cos(5 * x[i])
        result += 0.2 * chaotic_term
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result