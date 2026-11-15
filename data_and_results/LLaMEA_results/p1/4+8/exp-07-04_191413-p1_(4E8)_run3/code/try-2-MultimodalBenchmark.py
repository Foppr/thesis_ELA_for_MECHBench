import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Sum of quadratic terms with different scales and offsets
        result = 0.0
        
        # Global minimum at origin
        result += np.sum(x**2)
        
        # Add multiple local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add more complex interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Add noise-like component to increase complexity
        result += 0.05 * np.sum(np.sin(10 * x) + np.cos(7 * x))
        
        return result