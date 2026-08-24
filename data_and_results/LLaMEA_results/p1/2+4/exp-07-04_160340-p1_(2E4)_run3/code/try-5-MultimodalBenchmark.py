import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic term
        result = np.sum(x**2)
        
        # Add multiple local minima using higher frequency sinusoidal terms
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Add a more complex saddle point structure with interaction terms
        if self.dim >= 2:
            for i in range(self.dim - 1):
                result += 0.1 * (x[i]**2 - x[i+1]**2)**2
                
        # Add a periodic component to increase multimodality
        result += 0.15 * np.sum(np.sin(2 * np.pi * x / 1.5))
        
        # Add a small noise-like component to increase landscape complexity
        result += 0.02 * np.sum(np.sin(15 * x) * np.cos(13 * x))
        
        return result