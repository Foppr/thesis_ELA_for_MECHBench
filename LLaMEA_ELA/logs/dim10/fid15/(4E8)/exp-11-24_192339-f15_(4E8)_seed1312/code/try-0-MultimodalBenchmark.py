import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squared terms with different frequencies
        result = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal components
        for i in range(1, min(6, self.dim + 1)):
            result += 0.1 * np.sin(i * np.pi * x_normalized) * np.cos(i * np.pi * x_normalized)
            
        # Add a global minimum at origin with additional penalty terms
        penalty = 0.01 * np.sum(x_normalized**4)
        
        return result + penalty