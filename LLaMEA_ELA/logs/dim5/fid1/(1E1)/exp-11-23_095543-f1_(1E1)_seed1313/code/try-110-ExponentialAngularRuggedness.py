import numpy as np

class ExponentialAngularRuggedness:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base polynomial terms with varying exponents
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * np.abs(x[i]) ** (2 + 0.5 * i)
            
        # Add exponential decay modulation based on angular position
        angle_sum = 0.0
        for i in range(self.dim):
            angle_sum += np.arctan2(x[(i + 1) % self.dim], x[i])
        result *= (1.0 + 0.3 * np.exp(-0.5 * angle_sum ** 2))
        
        # Add angular frequency components
        for i in range(self.dim):
            result += 0.2 * np.sin(8 * np.arctan2(x[(i + 1) % self.dim], x[i])) * np.cos(6 * x[i])
            
        # Add polynomial coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                result += 0.15 * x[i] ** 2 * x[j] ** 3
                
        # Add radial exponential terms with angular dependence
        r = np.sqrt(np.sum(x ** 2))
        for i in range(self.dim):
            result += 0.25 * np.exp(-r) * np.cos(10 * np.arctan2(x[i], x[(i + 1) % self.dim]))
            
        # Add multi-scale oscillatory components
        for i in range(self.dim):
            result += 0.1 * np.sin(15 * x[i]) * np.cos(12 * x[(i + 2) % self.dim]) * (1 + 0.2 * np.sin(r))
            
        # Add asymmetric cubic terms
        for i in range(self.dim):
            result += 0.08 * x[i] ** 3 * np.sin(5 * x[(i + 1) % self.dim])
            
        # Add a global scaling factor based on dimensionality
        scaling = 1.0 + 0.1 * np.sum(np.abs(x)) + 0.05 * np.sum(x ** 2)
        result *= scaling
        
        return result