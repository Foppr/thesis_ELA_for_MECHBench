import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add highly chaotic sinusoidal components with cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[j]) * np.sin(2 * (x[i] + x[j]))
        
        # Add saddle point structure with polynomial terms
        for i in range(self.dim):
            result += 0.2 * x[i]**4 - 0.5 * x[i]**3 + 0.1 * x[i]**2
        
        # Add non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.4 * np.sin(10 * sum_x) * np.cos(8 * sum_x)
        
        # Add global minimum penalty with exponential scaling
        result += 0.05 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        return result