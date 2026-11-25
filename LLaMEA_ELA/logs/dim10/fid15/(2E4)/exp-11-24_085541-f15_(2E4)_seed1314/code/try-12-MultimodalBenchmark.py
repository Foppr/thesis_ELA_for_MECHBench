import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple global minima with exponential scaling and sine modulation
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.05 * x[i]**2) * np.sin(15 * x[i])**3
            
        # Add chaotic oscillations with varying frequencies and damping factors
        for i in range(self.dim):
            result += 0.4 * np.sin(x[i] * np.exp(0.7 * i)) * np.cos(x[i] * np.exp(0.4 * i)) * np.exp(-0.1 * i)
            
        # Add saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.3 * x[i]**5 - 0.15 * x[i]**4 + 0.05 * x[i]**3
            
        # Add a complex penalty term with mixed norms and adaptive scaling
        result += 0.08 * np.sum(np.abs(x)**3.5) + 0.03 * np.sum(np.abs(x)**6)
        
        # Add cross-dimensional interactions for increased complexity with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j])) * np.exp(-0.02 * (i+j))
                
        # Add a global scaling factor that increases with dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        return result