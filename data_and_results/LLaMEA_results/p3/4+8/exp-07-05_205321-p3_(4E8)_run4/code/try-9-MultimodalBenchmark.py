import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Periodic terms with varying frequencies to create multiple local minima
        periodic = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Exponential decay term to create flat regions
        exponential = np.sum(np.exp(-0.5 * x_scaled**2))
        
        # Interaction term between dimensions
        interaction = np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Combine all terms with different weights
        return 0.2 * quadratic + 0.4 * periodic + 0.3 * exponential + 0.1 * interaction + 2.0