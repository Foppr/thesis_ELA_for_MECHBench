import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Exponentially decaying sinusoidal waves with multiple peaks
        waves = 0.0
        for i in range(self.dim):
            waves += np.exp(-0.1 * np.abs(x[i])) * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Central repulsive force to create challenging landscape
        repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x**2))
        if dist_from_origin > 0:
            repulsion = 2.0 * np.exp(-dist_from_origin / 2.0)
            
        # Additional cubic terms for increased nonlinearity
        cubic = 0.0
        for i in range(self.dim):
            cubic += 0.01 * x[i]**3
            
        return basin + waves - repulsion + cubic