import numpy as np

class HyperbolicSinusoidalFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        result = 0.0
        
        # Base hyperbolic paraboloid terms
        for i in range(self.dim):
            result += x[i]**2 - 2 * x[i] * np.sin(x[i])
            
        # Add sinusoidal modulations to create multiple local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                
        # Add a global sinusoidal modulation that changes the landscape
        result += 2 * np.sin(np.sum(x) / self.dim)
        
        # Add noise-like component to increase complexity
        for i in range(self.dim):
            result += 0.1 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        return result