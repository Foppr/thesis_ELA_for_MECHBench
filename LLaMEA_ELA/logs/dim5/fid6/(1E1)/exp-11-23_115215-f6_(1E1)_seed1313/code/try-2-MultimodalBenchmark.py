import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sine waves with different frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.05 * np.sin(2 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.015 * np.sum(np.abs(x)) + 0.002 * np.sum(x**4) + 0.0005 * np.sum(x**6)
        
        return f_val