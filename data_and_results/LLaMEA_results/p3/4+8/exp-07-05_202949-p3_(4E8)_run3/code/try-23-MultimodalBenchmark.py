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
            f_val += 0.3 * np.sin(12 * x[i]) * np.cos(8 * x[i]) * np.sin(5 * x[i])
            
        # Add polynomial penalty terms for increased complexity
        f_val += 0.15 * np.sum(x**4)
        
        # Add cross-dimensional interactions with varying weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
        
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.03 * np.sum(np.abs(x)**1.7)
        
        # Add a secondary global minimum structure with more complex interactions
        f_val += 0.04 * np.sum(np.sin(3 * x)**2)
        
        # Add adaptive penalty based on variable correlations
        for i in range(self.dim):
            f_val += 0.02 * np.sin(4 * x[i])**2 * np.cos(2 * x[i])
            
        # Add a complex interaction term that varies with dimensionality
        if self.dim > 1:
            f_val += 0.05 * np.sum((x[:-1] - x[1:])**2 * np.sin(x[:-1] + x[1:]))
        
        return f_val