import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin (0,0,...,0) with value 0
        result = 0.0
        
        # Add exponentially increasing oscillations
        for i in range(self.dim):
            result += np.exp(0.5 * np.abs(x[i])) * np.sin(10.0 * x[i])**2
            
        # Add polynomial basins with varying degrees
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.05 * x[i]**6
            
        # Add cross-dimensional interactions with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] * x[j]) * np.cos(2.0 * (x[i] + x[j]))
                
        # Add a complex sinusoidal component with multiple frequencies
        for i in range(self.dim):
            result += 2.0 * np.sin(15.0 * x[i]) * np.cos(7.0 * x[i]) * np.sin(3.0 * x[i])
            
        # Add a penalty term that increases with distance from origin
        distance_penalty = 0.01 * np.sum(x**2) + 0.001 * np.sum(x**4)
        result += distance_penalty
        
        return result