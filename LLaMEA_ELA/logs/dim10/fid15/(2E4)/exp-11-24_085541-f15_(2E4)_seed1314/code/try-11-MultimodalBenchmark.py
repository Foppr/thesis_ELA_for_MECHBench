import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple global minima with exponential scaling and sinusoidal modulation
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.15 * x[i]**2) * np.sin(15 * x[i])**3
            
        # Add chaotic oscillations with varying frequencies and amplitude modulation
        for i in range(self.dim):
            result += 0.4 * np.sin(x[i] * np.exp(0.7 * i)) * np.cos(x[i] * np.exp(0.4 * i)) * np.sin(0.5 * x[i])
            
        # Add saddle point structure with polynomial terms and cross-terms
        for i in range(self.dim):
            result += 0.3 * x[i]**5 - 0.15 * x[i]**4 + 0.05 * x[i]**3
            
        # Add a complex penalty term with mixed norms and adaptive scaling
        result += 0.1 * np.sum(np.abs(x)**4) + 0.05 * np.sum(np.abs(x)**6)
        
        # Add cross-dimensional interactions for increased complexity with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j])) * np.exp(-0.05 * (i+j))
                
        # Add a periodic component with irregular frequency pattern
        for i in range(self.dim):
            result += 0.25 * np.sin(2 * np.pi * x[i] * (1 + 0.1 * np.sin(i))) * np.cos(3 * np.pi * x[i])
            
        # Add a logarithmic barrier near boundaries to encourage exploration
        result += 0.1 * np.sum(np.log(25.0 - x**2))
        
        return result