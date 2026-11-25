import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add exponential decay terms with trigonometric perturbations
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.1 * np.abs(x[i])) * np.sin(2 * np.pi * x[i])
            
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.cos(x[i] * x[j])
                
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**6
            
        # Add trigonometric cross-terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2)
                
        # Add a global scaling factor based on the sum of absolute values
        result *= (1 + 0.1 * np.sum(np.abs(x)))
        
        return result