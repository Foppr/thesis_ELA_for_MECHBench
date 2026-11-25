import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced logistic map based fractal structure with increased chaos
        logistic_map = 0.0
        r = 3.99
        for i in range(15):
            logistic_map += np.sin(r * x_norm * (1 - x_norm))
        f2 = 0.3 * np.sum(logistic_map**2)
        
        # Modified multi-scale harmonic oscillations with higher frequencies
        f3 = 0.2 * np.sum(np.sin(25 * x_norm) + np.sin(50 * x_norm) + np.sin(100 * x_norm))
        
        # Strengthened self-similar cubic polynomial interactions
        f4 = 0.15 * np.sum(x_norm**3)
        
        # Enhanced cross-dimension coupling with exponential weights
        cross_term = 0.1 * np.sum(np.exp(-0.5 * np.abs(x_norm[:-1])) * x_norm[1:])
        
        # Modified asymmetric saddle points with sharper transitions
        f5 = 0.2 * np.sum(np.where(x_norm > 0, x_norm**2.5, -x_norm**2.5))
        
        return f1 + f2 + f3 + f4 + cross_term + f5