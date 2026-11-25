import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Tent map based fractal structure
        tent_map = 0.0
        for i in range(15):
            tent_map += np.tanh(4 * x_norm * (1 - np.abs(x_norm)))
        f2 = 0.3 * np.sum(tent_map**2)
        
        # Multi-scale fractal noise with varying amplitudes
        f3 = 0.25 * np.sum(np.sin(30 * x_norm) + np.sin(90 * x_norm) + np.sin(270 * x_norm))
        
        # Asymmetric hyperbolic tangent interactions
        f4 = 0.2 * np.sum(np.where(x_norm > 0, np.tanh(x_norm), -np.tanh(-x_norm)))
        
        # Coupled polynomial interactions with exponential weights
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            poly_interaction += np.exp(-0.5 * (i + 1)) * (x_norm[i]**4 + x_norm[i+1]**4)
        f5 = 0.15 * np.sum(poly_interaction)
        
        # Cross-dimension coupling with chaotic sine waves
        cross_term = 0.1 * np.sum(np.sin(50 * x_norm[:-1]) * np.cos(50 * x_norm[1:]))
        
        # Degenerate saddle points with piecewise cubic functions
        f6 = 0.1 * np.sum(np.where(x_norm > 0, x_norm**3, -x_norm**3))
        
        return f1 + f2 + f3 + f4 + f5 + cross_term + f6