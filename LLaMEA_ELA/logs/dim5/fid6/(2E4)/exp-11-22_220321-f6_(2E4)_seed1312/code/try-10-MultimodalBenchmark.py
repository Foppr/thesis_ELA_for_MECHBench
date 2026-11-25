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
            
        # Add multiple local minima using sine waves with exponential frequency growth
        for i in range(self.dim):
            freq = 2 ** (i % 4)  # Exponentially increasing frequencies
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add a complex penalty term with multiple peaks
        penalty = 0.0
        for i in range(self.dim):
            # Create multiple local minima around ±2.0 and ±4.0
            penalty += (x[i] - 2.0)**6 + (x[i] + 2.0)**6 + (x[i] - 4.0)**6 + (x[i] + 4.0)**6
            
        # Add cross-dimensional interaction terms for increased complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.3 * np.sin(x[i]) * np.cos(x[j]) * (i + j)
                
        return result + 0.02 * penalty + 0.1 * cross_term