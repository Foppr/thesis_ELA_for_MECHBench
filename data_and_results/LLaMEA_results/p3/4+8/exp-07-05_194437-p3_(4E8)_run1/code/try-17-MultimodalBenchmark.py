import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add quadratic term for conditioning
        result += 0.1 * np.sum(x**2)
        
        # Add periodic terms with varying frequencies
        for i in range(self.dim):
            result += 5 * np.sin(2 * np.pi * x[i] / (1 + 0.1 * i)) * np.cos(3 * np.pi * x[i] / (1 + 0.2 * i))
        
        # Add a more complex interaction term
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-interaction
                result += 2 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.01 * (x[i] - x[j])**2)
        
        # Add a global shaping term
        result += 0.01 * np.sum(np.abs(x)**3)
        
        # Add a noise-like component for added complexity
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(5 * x[i])
        
        return result