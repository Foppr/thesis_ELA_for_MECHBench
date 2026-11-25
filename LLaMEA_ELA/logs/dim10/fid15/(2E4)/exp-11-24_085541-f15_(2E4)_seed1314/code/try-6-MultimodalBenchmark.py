import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple global minima with exponential scaling
        for i in range(self.dim):
            result += 0.5 * np.exp(-0.1 * x[i]**2) * np.sin(10 * x[i])**2
            
        # Add chaotic oscillations with varying frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(x[i] * np.exp(0.5 * i)) * np.cos(x[i] * np.exp(0.3 * i))
            
        # Add saddle point structure with polynomial terms
        for i in range(self.dim):
            result += 0.2 * x[i]**4 - 0.1 * x[i]**3
            
        # Add a complex penalty term with mixed norms
        result += 0.05 * np.sum(np.abs(x)**4) + 0.02 * np.sum(np.abs(x)**5)
        
        # Add cross-dimensional interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        return result