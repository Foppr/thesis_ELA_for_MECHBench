import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with increasing coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i]**2
        
        # High-frequency sinusoidal perturbations with exponential growth
        for i in range(self.dim):
            freq = 10**(i % 3 + 1)  # Increasing frequencies: 10, 100, 1000, 10, 100, ...
            result += 0.2 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
        
        # Complex cross-dimensional interactions with varying weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                weight = (i + 1) * (j + 1) * 0.005
                result += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add a global scaling factor to increase landscape complexity
        result *= (1.0 + 0.1 * np.sum(np.abs(x)) / self.dim)
        
        return result