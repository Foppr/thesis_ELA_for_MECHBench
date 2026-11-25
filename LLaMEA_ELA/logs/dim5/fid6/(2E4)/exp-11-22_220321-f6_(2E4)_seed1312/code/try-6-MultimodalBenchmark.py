import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with exponentially increasing coefficients
        for i in range(self.dim):
            result += (x[i] ** 2) * (2 ** i)
            
        # Add highly oscillatory local minima using sine waves with exponentially increasing frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 4)
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add cross-dimensional interaction terms with high-frequency oscillations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(10 * x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add a complex penalty term with multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i] - 2.0)**6 + (x[i] + 2.0)**6 + 0.5 * np.sin(10 * x[i])
            
        # Add a chaotic component using logistic map-like behavior
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(100 * x[i]) * np.cos(50 * x[(i + 1) % self.dim])
            
        return result + 0.02 * penalty + 0.005 * chaos