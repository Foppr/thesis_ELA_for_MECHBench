import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Logarithmic barrier terms creating sharp ridges and valleys
        log_barrier = 0.5 * np.sum(np.log(1.0 + 0.1 * x_norm**2))
        
        # Complex harmonic interactions with varying frequencies
        f2 = 0.3 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Saddle-point structure with mixed positive and negative curvature
        saddle = 0.2 * np.sum(x_norm**2 * np.sin(5 * np.pi * x_norm))
        
        # High-order polynomial with alternating signs
        f3 = 0.1 * np.sum(np.abs(x_norm)**5)
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_coupling = 0.15 * np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                      np.cos(2 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Asymmetric oscillations creating non-symmetric local minima
        asym = 0.25 * np.sum(np.sin(3 * np.pi * x_norm) * np.exp(-x_norm**2))
        
        return f1 + log_barrier + f2 + saddle + f3 + cross_coupling + asym