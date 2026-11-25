import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple nested oscillatory components with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i]) + \
                     0.3 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + \
                     0.2 * np.sin(15 * x[i])
        
        # Add complex interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                result += 0.1 * np.sin(x[i] + x[j]) * np.cos(2 * (x[i] - x[j]))
        
        # Add multiple global minima with different basins of attraction
        for i in range(self.dim):
            result += 0.05 * (x[i]**8 - 2*x[i]**6 + x[i]**4)
            
        # Add a rugged terrain with many local minima
        for i in range(self.dim):
            result += 0.02 * np.sin(50 * x[i]) * np.cos(30 * x[i])
        
        # Add a penalty term to avoid boundary regions
        penalty = 0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 10 * (abs(x[i]) - 4.5)**2
        result += penalty
        
        return result