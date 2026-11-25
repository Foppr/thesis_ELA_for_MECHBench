import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Exponentially decaying sinusoidal terms creating rugged landscape
        rugged = 0.0
        for i in range(self.dim):
            rugged += np.exp(-0.1 * np.abs(x[i])) * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Additional polynomial terms for increased complexity and non-uniformity
        poly = 0.0
        for i in range(self.dim):
            poly += 0.5 * x[i]**4 - 2.0 * x[i]**3 + 1.5 * x[i]**2
            
        return basin + rugged + poly