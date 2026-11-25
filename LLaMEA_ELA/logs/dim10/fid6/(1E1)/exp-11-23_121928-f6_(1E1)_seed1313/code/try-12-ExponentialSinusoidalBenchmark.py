import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay term that encourages convergence
        exp_term = np.sum(np.exp(-x_norm**2))
        
        # Sinusoidal modulation with varying frequencies
        sin_term = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Quadratic saddle point structure
        quad_term = np.sum(x_norm**2 - 0.1 * x_norm**4)
        
        # Cross-term interaction creating complex dependencies
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(np.pi * x_norm[:-1]))
        
        # Combine all terms with different weights
        return 0.3 * exp_term + 0.4 * sin_term - 0.2 * quad_term + 0.1 * cross_term + 0.05 * np.sum(x_norm**6)