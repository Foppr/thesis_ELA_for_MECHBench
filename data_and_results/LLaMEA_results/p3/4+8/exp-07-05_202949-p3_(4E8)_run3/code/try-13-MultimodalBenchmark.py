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
            f_val += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
        # Add polynomial penalty terms for increased complexity
        f_val += 0.1 * np.sum(x**4)
        
        # Add cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.02 * np.sum(np.abs(x)**1.5)
        
        # Add a secondary global minimum structure
        f_val += 0.03 * np.sum(np.sin(2 * x)**2)
        
        return f_val