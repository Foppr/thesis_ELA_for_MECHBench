import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Combines quadratic, sinusoidal, and exponential terms
        result = 0.0
        
        # Quadratic term (global minimum at origin)
        result += np.sum(x**2)
        
        # Sinusoidal terms to create multiple local minima
        for i in range(self.dim):
            result += 10 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
        
        # Exponential terms to increase function complexity
        for i in range(self.dim):
            result += 5 * np.exp(-0.1 * x[i]**2)
        
        # Cross-terms to create interaction between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j])
        
        return result