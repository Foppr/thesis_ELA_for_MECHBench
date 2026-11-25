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
            freq = 2 ** (i % 5)  # Exponentially increasing frequencies
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add chaotic component for increased complexity
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(x[i] * np.pi * (i + 1)) * np.cos(x[(i + 2) % self.dim] * np.pi * (i + 1))
            
        # Add a complex penalty term with multiple local optima
        penalty = 0.0
        for i in range(self.dim):
            # Multiple polynomial terms creating complex landscape
            penalty += (x[i] ** 6 + 0.5 * x[i] ** 4 + 0.1 * x[i] ** 2) * (i + 1)
            
        # Add cross-dimensional interactions with chaotic influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(x[i]) * np.cos(x[j]) * (i + j) * (1 + 0.1 * chaos)
                
        return result + 0.03 * penalty + 0.05 * chaos