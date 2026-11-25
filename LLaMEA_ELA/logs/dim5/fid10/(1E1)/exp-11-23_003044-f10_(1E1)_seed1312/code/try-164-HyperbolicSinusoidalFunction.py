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
            
        # Add sinusoidal modulations to create multiple minima
        for i in range(self.dim):
            result += 0.5 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Interaction terms between dimensions creating complex landscape
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                
        # Add a global sinusoidal modulation to increase complexity
        result += 0.2 * np.sin(np.sum(x)**2)
        
        # Scale and shift to ensure proper conditioning
        result = result * (1 + 0.1 * np.sum(np.abs(x)))
        
        return result