import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced logistic map based fractal structure with higher chaos parameter
        logistic_map = 0.0
        r = 3.99
        for i in range(15):
            logistic_map += np.sin(r * x_norm * (1 - x_norm))
        f2 = 0.3 * np.sum(logistic_map**2)
        
        # Modified multi-scale harmonic oscillations with increased frequency multiples
        f3 = 0.2 * np.sum(np.sin(25 * x_norm) + np.sin(50 * x_norm) + np.sin(100 * x_norm))
        
        # Adjusted self-similar cubic polynomial interactions with higher order terms
        f4 = 0.15 * np.sum(x_norm**3)
        
        # Modified cross-dimension coupling with different exponential weights
        cross_term = 0.08 * np.sum(np.exp(-0.5 * np.abs(x_norm[:-1])) * x_norm[1:])
        
        # Enhanced asymmetric saddle points with modified piecewise function
        f5 = 0.12 * np.sum(np.where(x_norm > 0, x_norm**2.5, -x_norm**2.5))
        
        return f1 + f2 + f3 + f4 + cross_term + f5