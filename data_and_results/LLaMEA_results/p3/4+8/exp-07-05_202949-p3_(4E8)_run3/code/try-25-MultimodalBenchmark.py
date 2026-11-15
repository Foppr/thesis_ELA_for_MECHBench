import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple interacting local minima using high-frequency sinusoidal terms
        for i in range(self.dim):
            f_val += 0.7 * np.sin(15 * x[i]) * np.cos(11 * x[i]) * np.sin(5 * x[i])
            
        # Add polynomial penalty terms for increased complexity
        f_val += 0.15 * np.sum(x**4)
        
        # Add cubic terms for additional nonlinearity
        f_val += 0.05 * np.sum(x**3)
        
        # Add cross-dimensional interactions with higher frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(2 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 2 * x[j])
        
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.03 * np.sum(np.abs(x)**1.7)
        
        # Add a secondary global minimum structure
        f_val += 0.04 * np.sum(np.sin(3 * x)**2)
        
        return f_val