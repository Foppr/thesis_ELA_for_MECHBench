import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term with higher conditioning
        quadratic = np.sum(x**2) / self.dim
        
        # Highly multimodal periodic component with exponential scaling
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.exp(2 * np.sin(15 * np.pi * x[i] ** 3)) + 0.7 * np.exp(3 * np.sin(25 * np.pi * x[i] ** 3))
        
        # Complex basin with saddle points and cross-dimensional interactions
        basin = 0.05 * (np.sum((x - 1.0)**2) + 0.1 * np.sum(x[:-1] * x[1:]) + 0.05 * np.sum((x**2 - 1.0)**2))
        
        # Add cross-dimensional interaction terms
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(np.pi * (x[i] + x[j])) ** 6
        
        return quadratic + periodic + basin + cross_dim