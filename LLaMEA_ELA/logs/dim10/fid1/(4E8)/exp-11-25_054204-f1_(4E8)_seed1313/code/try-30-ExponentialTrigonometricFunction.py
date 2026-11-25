import numpy as np

class ExponentialTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = np.sum(x**2)
        
        # Add exponential decay terms with trigonometric modulation
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.1 * np.abs(x[i])) * np.sin(2 * np.pi * x[i])
            
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.cos(x[i] * x[j])
                
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**6
            
        # Add mixed trigonometric-polynomial interactions
        for i in range(self.dim):
            result += 0.2 * np.sin(3 * x[i]) * (1 + 0.1 * x[i]**4)
            
        # Add cross-dimensional polynomial terms with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**2) * (x[j]**4) * np.exp(-0.02 * (x[i] + x[j])**2)
                
        return result