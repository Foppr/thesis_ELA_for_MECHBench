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
            f_val += 0.2 * np.sin(8 * x[i]) * np.cos(3 * x[i]) + 0.07 * np.sin(3 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.02 * np.sum(np.abs(x)) + 0.003 * np.sum(x**4) + 0.001 * np.sum(x**6)
        
        return f_val