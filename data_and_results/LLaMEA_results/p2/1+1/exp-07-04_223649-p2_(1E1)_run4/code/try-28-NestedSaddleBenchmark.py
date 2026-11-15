import numpy as np

class NestedSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial scaling
        r = np.sqrt(np.sum(x**2))
        radial = 0.5 * r**2 + 0.1 * r**4 + 0.02 * r**6
        
        # Saddle point structure with alternating signs
        saddle = 0.0
        for i in range(self.dim):
            saddle += (-1)**i * x[i]**2 * np.sin(x[i])
            
        # Polynomial chaos component with mixed degrees
        chaos = 0.0
        for i in range(self.dim):
            chaos += (x[i]**3 - 3*x[i]) * np.cos(0.5 * x[i])
            
        # Nested oscillatory structure
        nested = 0.0
        for i in range(self.dim):
            nested += np.sin(2.0 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i])
            
        # Interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += 0.3 * x[i] * x[i+1] * np.sin(0.2 * x[i] * x[i+1])
            
        # Global minimum at origin with additional perturbation
        result = radial + saddle + chaos + nested + interaction
        
        return result