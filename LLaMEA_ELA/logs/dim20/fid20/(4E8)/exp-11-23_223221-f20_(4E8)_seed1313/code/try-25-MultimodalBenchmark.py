import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Radial basis functions with varying widths
        for i in range(self.dim):
            # Different width for each dimension
            width = 1.0 + 0.5 * np.sin(i)
            result += np.exp(-width * x[i]**2) * np.cos(2 * np.pi * x[i])
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction term with cosine modulation
                result += 0.1 * np.cos(3 * x[i]) * np.sin(2 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add a quadratic basin term to encourage convergence
        result += 0.05 * np.sum(x**2)
        
        # Normalize by dimension to keep scale reasonable
        return result / self.dim