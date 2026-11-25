import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squared terms with different weights and offsets
        result = np.sum(x_norm**2)
        
        # Add multiple local minima using sinusoidal components
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[(i+1) % self.dim])
            
        # Add a global minimum at origin with additional penalty terms
        result += 0.01 * np.sum(np.abs(x_norm)**3)
        
        return result