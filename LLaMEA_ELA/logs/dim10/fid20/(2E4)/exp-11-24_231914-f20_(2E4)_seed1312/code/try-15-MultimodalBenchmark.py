import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Periodic multimodal term with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(11 * np.pi * x[i]) ** 2 + 0.5 * np.sin(5 * np.pi * x[i]) ** 2
        
        # Add interaction terms between dimensions with cubic terms
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**2 + 0.3 * (x[i] - x[i+1])**3
        
        # Add cross-dimensional interaction
        cross_term = 0.0
        for i in range(0, self.dim - 2, 2):
            cross_term += x[i] * x[i+1] + 0.2 * x[i] * x[i+2]
        
        # Shifted global minimum term
        shift = np.sum((x - 1.0)**3) / self.dim
        
        # Combine terms to create challenging landscape
        return quadratic + 0.25 * periodic + 0.1 * interaction + 0.05 * cross_term + 0.1 * shift