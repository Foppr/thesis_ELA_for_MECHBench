import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Enhanced multimodal structure with higher frequency sinusoids
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        # Add coupling between dimensions to create more complex landscape
        if self.dim >= 2:
            for i in range(self.dim - 1):
                result += 0.1 * (x[i]**2 + x[i+1]**2) * np.sin(2 * (x[i] - x[i+1]))
            
        # Add a periodic saddle structure to increase difficulty
        if self.dim >= 3:
            for i in range(0, self.dim - 2, 3):
                result += 0.05 * np.sin(x[i]) * np.cos(x[i+1]) * np.sin(x[i+2])
                
        return result