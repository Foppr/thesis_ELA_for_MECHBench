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
            result += 1.2 * np.exp(-0.03 * x[i]**2) * np.sin(20 * x[i])**4
            
        # Add chaotic oscillations with varying frequencies and damping factors
        for i in range(self.dim):
            result += 0.6 * np.sin(x[i] * np.exp(0.8 * i)) * np.cos(x[i] * np.exp(0.5 * i)) * np.exp(-0.15 * i)
            
        # Add saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.4 * x[i]**6 - 0.2 * x[i]**5 + 0.08 * x[i]**4
            
        # Add a complex penalty term with mixed norms and adaptive scaling
        result += 0.12 * np.sum(np.abs(x)**4) + 0.05 * np.sum(np.abs(x)**7)
        
        # Add cross-dimensional interactions for increased complexity with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i] + x[j])) * np.exp(-0.03 * (i+j))
                
        # Add a global scaling factor that increases with dimensionality
        result *= (1.0 + 0.15 * self.dim)
        
        return result