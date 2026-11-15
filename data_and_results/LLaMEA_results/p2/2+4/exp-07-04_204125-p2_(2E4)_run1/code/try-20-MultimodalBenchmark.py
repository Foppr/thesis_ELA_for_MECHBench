import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Add multiple quadratic terms with different scales and offsets
        for i in range(self.dim):
            # Main quadratic term
            result += (x[i] - 1.0)**2
            
            # Additional terms to create multimodality
            if i < self.dim - 1:
                result += 0.5 * (x[i] + x[i+1])**2
            
            # Add sinusoidal perturbations to create more complex landscape
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add a small noise term to make it non-convex
        result += 0.01 * np.sum(x**4)
        
        return result