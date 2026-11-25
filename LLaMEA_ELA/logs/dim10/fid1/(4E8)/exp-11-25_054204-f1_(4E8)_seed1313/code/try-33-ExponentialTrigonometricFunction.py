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
            result += 0.4 * np.exp(-0.15 * np.abs(x[i])) * np.sin(3 * np.pi * x[i])
            
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.exp(-0.08 * (x[i]**2 + x[j]**2)) * np.cos(x[i] * x[j])
                
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.08 * x[i]**6
            
        # Add mixed trigonometric-polynomial interactions
        for i in range(self.dim):
            result += 0.25 * np.sin(4 * x[i]) * (1 + 0.15 * x[i]**4)
            
        # Add cross-dimensional polynomial terms with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * (x[i]**3) * (x[j]**5) * np.exp(-0.03 * (x[i] + x[j])**2)
                
        # Add Gaussian perturbations to increase multimodality
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.5 * (x[i] - 2)**2) * np.sin(5 * x[i])
            
        # Add a global scaling factor to improve conditioning
        result *= (1 + 0.1 * np.sum(np.abs(x)))
        
        return result