import numpy as np

class ExponentialTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = np.sum(x**2)
        
        # Add hyperbolic tangent exponential decay terms with trigonometric modulation
        for i in range(self.dim):
            result += 0.5 * np.tanh(0.2 * x[i]) * np.exp(-0.1 * np.abs(x[i])) * np.sin(4 * np.pi * x[i])
            
        # Add cross-dimensional hyperbolic interactions with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.tanh(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.cos(2 * x[i] * x[j])
                
        # Add higher-order polynomial terms with variable exponents
        for i in range(self.dim):
            result += 0.1 * x[i]**7 * np.exp(-0.02 * np.abs(x[i]))
            
        # Add mixed trigonometric-polynomial interactions with adaptive scaling
        for i in range(self.dim):
            result += 0.3 * np.sin(5 * x[i]) * (1 + 0.2 * x[i]**5) * np.exp(-0.03 * x[i]**2)
            
        # Add cross-dimensional polynomial terms with hyperbolic weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * (x[i]**4) * (x[j]**6) * np.tanh(0.1 * (x[i] + x[j])) * np.exp(-0.04 * (x[i] - x[j])**2)
                
        # Add Gaussian perturbations with variable widths and frequencies
        for i in range(self.dim):
            result += 0.15 * np.exp(-0.3 * (x[i] - 1.5)**2) * np.sin(6 * x[i])
            
        # Add adaptive scaling based on dimensionality and distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.15 * np.log(1 + dist_from_origin) + 0.05 * self.dim)
        
        return result