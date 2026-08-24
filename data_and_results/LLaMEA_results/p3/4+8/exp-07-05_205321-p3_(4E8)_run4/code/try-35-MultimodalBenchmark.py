import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequency to create more local minima
        sinusoidal = np.sum(np.sin(9 * np.pi * x_norm))
        
        # Product term with different frequency to create stronger interactions
        product = np.prod(np.cos(0.4 * np.pi * x_norm))
        
        # Additional quintic term for increased nonlinearity
        quintic = np.sum(x_norm**5)
        
        # Shifted global minimum to increase difficulty
        shift = 0.15 * np.sum((x_norm - 0.15)**2)
        
        # Combine terms with different weights
        return 0.1 * quadratic + 0.3 * sinusoidal + 0.4 * product + 0.08 * quintic + 0.07 * shift + 1.0