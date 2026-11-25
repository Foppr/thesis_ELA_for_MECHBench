import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add multiple local minima using sine waves with exponentially increasing frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 4)  # Exponentially increasing frequencies
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add a complex penalty term with multiple local optima
        penalty = 0.0
        for i in range(self.dim):
            # Multiple polynomial terms creating complex landscape
            penalty += (x[i] ** 6 + 0.5 * x[i] ** 4 + 0.1 * x[i] ** 2) * (i + 1)
            
        # Add cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i]) * np.cos(x[j]) * (i + j)
                
        return result + 0.02 * penalty