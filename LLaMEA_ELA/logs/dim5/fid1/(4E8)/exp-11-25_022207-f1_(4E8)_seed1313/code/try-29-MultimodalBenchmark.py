import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal modulations creating many local minima
        f2 = 0.3 * np.sum(np.sin(15 * np.pi * x_norm))
        
        # Additional complex modulation with multiple frequencies
        f3 = 0.2 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm))
        
        # Quartic and sextic polynomial terms for increased curvature
        f4 = 0.1 * np.sum(x_norm**4)
        f5 = 0.05 * np.sum(x_norm**6)
        
        # Cross-terms to create complex interactions between dimensions
        cross_term = 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Exponential decay modulation to control the landscape smoothness
        exp_mod = 0.05 * np.sum(np.exp(-x_norm**2))
        
        return f1 + f2 + f3 + f4 + f5 + cross_term + exp_mod