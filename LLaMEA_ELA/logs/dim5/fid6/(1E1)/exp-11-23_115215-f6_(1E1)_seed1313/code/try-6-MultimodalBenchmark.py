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
            f_val += 0.3 * np.sin(5 * x[i]) * np.cos(2 * x[i]) + 0.1 * np.sin(4 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.01 * np.sum(np.abs(x)) + 0.005 * np.sum(x**4) + 0.002 * np.sum(x**6)
        
        # Introduce additional complexity with higher frequency components and modified amplitudes
        for i in range(self.dim):
            f_val += 0.15 * np.sin(10 * x[i]) + 0.08 * np.cos(7 * x[i])
            
        return f_val