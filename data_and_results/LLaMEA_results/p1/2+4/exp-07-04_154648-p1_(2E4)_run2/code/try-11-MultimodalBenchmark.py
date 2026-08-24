import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay terms with varying rates
        for i in range(self.dim):
            result += np.exp(-0.5 * x[i]**2) * (i + 1)
        
        # Trigonometric wave interference creating multiple local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Cross-dimensional interactions with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                result += 0.1 * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a global scaling factor based on the sum of squares
        sum_sq = np.sum(x**2)
        result += 0.05 * sum_sq * np.sin(0.5 * sum_sq)
        
        # Add a chaotic component using a logistic map-like structure
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(np.pi * x[i]) * np.cos(np.pi * x[i])
        result += 0.2 * chaotic_term**2
        
        return result