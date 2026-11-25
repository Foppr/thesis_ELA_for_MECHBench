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
            periodic += np.sin(20 * np.pi * x[i]) ** 2
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**4
        
        # Add cubic interaction terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            cubic_interaction += (x[i] - x[i+2])**3
        
        # Add chaotic component using logistic map for enhanced complexity
        chaotic = 0.0
        r = 3.99
        for i in range(self.dim):
            if i == 0:
                chaotic += np.sin(r * x[i] * (1 - x[i])) ** 2
            else:
                chaotic += np.sin(r * x[i-1] * (1 - x[i-1])) ** 2
        
        # Shift global minimum to create more challenging landscape
        shift = 1.5
        
        # Combine terms to create challenging landscape
        return quadratic + 0.4 * periodic + 0.2 * interaction + 0.1 * cubic_interaction + 0.25 * chaotic + shift