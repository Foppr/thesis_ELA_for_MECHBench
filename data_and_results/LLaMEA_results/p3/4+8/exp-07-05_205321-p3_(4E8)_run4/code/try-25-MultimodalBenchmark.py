import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms to create varied curvature
        poly = np.sum(x_norm**4)
        
        # Exponential decay terms to introduce steep gradients
        exp_decay = np.sum(np.exp(-x_norm**2))
        
        # Trigonometric terms to generate multiple local minima
        trig = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Cross-term interaction to increase dimensionality challenge
        cross = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all terms with different weights
        return 0.2 * poly + 0.3 * exp_decay + 0.4 * trig + 0.1 * cross + 1.0