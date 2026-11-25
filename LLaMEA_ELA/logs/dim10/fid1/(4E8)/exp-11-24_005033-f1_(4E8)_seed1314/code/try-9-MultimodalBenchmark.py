import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize x to [-1, 1] for periodic functions
        x_norm = x / 5.0
        
        # Radial component with multiple local minima
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 0.5 * r**2 + 0.3 * np.sin(10 * r)
        
        # Periodic terms in each dimension
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.cos(2 * np.pi * x[i]) * np.sin(3 * np.pi * x[i])
            
        # Coupling between dimensions with varying strength
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += 0.1 * (x[i]**2 + x[i+1]**2) * np.sin(2 * np.pi * (x[i] + x[i+1]))
            
        # Adaptive difficulty based on dimensionality
        adaptivity = 1.0 + 0.1 * self.dim
        
        return adaptivity * (radial_term + periodic_term + coupling_term)