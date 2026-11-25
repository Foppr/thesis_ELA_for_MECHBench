import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Logistic map based fractal structure
        logistic_map = 0.0
        r = 3.95
        for i in range(10):
            logistic_map += np.sin(r * x_norm * (1 - x_norm))
        f2 = 0.2 * np.sum(logistic_map**2)
        
        # Multi-scale harmonic oscillations with varying frequencies
        f3 = 0.15 * np.sum(np.sin(20 * x_norm) + np.sin(40 * x_norm) + np.sin(80 * x_norm))
        
        # Self-similar cubic polynomial interactions
        f4 = 0.1 * np.sum(x_norm**3)
        
        # Cross-dimension coupling with exponentially varying weights
        cross_term = 0.05 * np.sum(np.exp(-np.abs(x_norm[:-1])) * x_norm[1:])
        
        # Asymmetric saddle points created by piecewise functions
        f5 = 0.1 * np.sum(np.where(x_norm > 0, x_norm**2, -x_norm**2))
        
        return f1 + f2 + f3 + f4 + cross_term + f5