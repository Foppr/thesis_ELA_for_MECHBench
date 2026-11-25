import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Sinusoidal oscillations creating multiple local minima
        sinusoidal = 2 * np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Gaussian peaks creating additional local optima
        gaussian = 0.5 * np.sum(np.exp(-10 * (x_norm - 0.3) ** 2) + 
                               np.exp(-10 * (x_norm + 0.4) ** 2))
        
        # Combine all terms with different weights
        return quadratic + sinusoidal + gaussian