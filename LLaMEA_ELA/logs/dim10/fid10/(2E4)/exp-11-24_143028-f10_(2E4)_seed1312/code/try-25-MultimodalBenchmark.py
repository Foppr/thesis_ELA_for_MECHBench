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
                result += 0.4 * np.sin(8 * x[i]) * np.cos(5 * x[j]) * np.sin(3 * (x[i] + x[j]))
        
        # Add saddle point structure with polynomial terms
        for i in range(self.dim):
            result += 0.3 * x[i]**4 - 0.6 * x[i]**3 + 0.15 * x[i]**2
        
        # Add non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.5 * np.sin(12 * sum_x) * np.cos(10 * sum_x)
        
        # Add global minimum penalty with exponential scaling
        result += 0.08 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Add additional chaotic cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(6 * x[i] * x[j]) * np.cos(3 * (x[i] - x[j]))
        
        return result