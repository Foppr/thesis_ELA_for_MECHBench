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
            f_val += 0.4 * np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.15 * np.sin(5 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.015 * np.sum(np.abs(x)) + 0.007 * np.sum(x**4) + 0.003 * np.sum(x**6)
        
        # Introduce additional complexity with higher frequency components and modified amplitudes
        for i in range(self.dim):
            f_val += 0.2 * np.sin(12 * x[i]) + 0.1 * np.cos(8 * x[i])
            
        # Add interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(2*x[i] + x[j]) * np.cos(x[i] - 2*x[j])
                
        return f_val