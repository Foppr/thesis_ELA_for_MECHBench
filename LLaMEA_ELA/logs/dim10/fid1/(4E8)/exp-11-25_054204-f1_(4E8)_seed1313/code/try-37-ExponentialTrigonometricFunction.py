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
            result += 0.35 * np.exp(-0.12 * np.abs(x[i])) * np.sin(2.5 * np.pi * x[i])
            
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.12 * np.exp(-0.06 * (x[i]**2 + x[j]**2)) * np.cos(1.5 * x[i] * x[j])
                
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.07 * x[i]**6
            
        # Add mixed trigonometric-polynomial interactions with cubic terms
        for i in range(self.dim):
            result += 0.25 * np.sin(3.2 * x[i]) * (1 + 0.15 * x[i]**4 + 0.05 * x[i]**3)
            
        # Add cross-dimensional polynomial terms with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.04 * (x[i]**2) * (x[j]**4) * np.exp(-0.025 * (x[i] + x[j])**2)
                
        return result