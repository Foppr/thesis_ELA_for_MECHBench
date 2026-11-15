import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for varying curvature
        self.coeffs = np.random.rand(dim) * 3 + 0.5
        self.saddle_points = np.random.rand(dim) * 8 - 4
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic exponential terms
        result = 0.0
        for i in range(self.dim):
            # Modified exponential decay with chaotic coefficients
            result += self.coeffs[i] * np.exp(-0.3 * (x[i] - self.saddle_points[i])**2)
            # Enhanced saddle point contribution with varying curvature
            result += 0.7 * (x[i] - self.saddle_points[i])**2 * np.sin(1.5 * x[i])
            # Chaotic gradient component with higher frequency
            result += 0.15 * np.sin(2.0 * self.coeffs[i] * x[i]) * np.cos(1.2 * x[i])
            
        # Add stronger coupling terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(2.0 * x[i] * x[j]) * (i + j)**1.5
                
        # Add global minimum at origin with penalty
        result += 0.002 * np.sum(x**6)
        
        return result