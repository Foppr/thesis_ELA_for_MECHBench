import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for varying curvature
        self.coeffs = np.random.rand(dim) * 2 + 1
        self.saddle_points = np.random.rand(dim) * 10 - 5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic exponential terms
        result = 0.0
        for i in range(self.dim):
            # Exponential decay with chaotic coefficients
            result += self.coeffs[i] * np.exp(-0.5 * (x[i] - self.saddle_points[i])**2)
            # Saddle point contribution with varying curvature
            result += 0.5 * (x[i] - self.saddle_points[i])**2 * np.sin(x[i])
            # Chaotic gradient component
            result += 0.1 * np.sin(self.coeffs[i] * x[i]) * np.cos(x[i])
            
        # Add coupling terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i] * x[j]) * (i + j)
                
        # Add global minimum at origin with penalty
        result += 0.001 * np.sum(x**6)
        
        return result