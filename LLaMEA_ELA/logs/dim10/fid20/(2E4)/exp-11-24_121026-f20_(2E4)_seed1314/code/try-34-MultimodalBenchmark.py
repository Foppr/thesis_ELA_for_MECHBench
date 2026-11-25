import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2, axis=0, keepdims=True))
        radial_term = np.sum(np.exp(-5 * r) * np.sin(3 * np.pi * r), axis=0)
        
        # High-frequency sinusoidal terms in each dimension
        sin_term = np.sum(np.sin(10 * x_norm)**2 + np.cos(7 * x_norm)**2, axis=0)
        
        # Saddle-point structure with polynomial interactions
        poly_term = np.sum(x_norm**4 - 2 * x_norm**2, axis=0)
        
        # Cross-term interaction to increase dimensionality complexity
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]), axis=0) if self.dim > 1 else 0
        
        # Barrier terms to create rugged terrain
        barrier = np.sum(1.0 / (1.0 + np.exp(-5 * (x_norm**2 - 0.5))), axis=0)
        
        # Global scaling and combination
        return 0.5 * radial_term + 0.3 * sin_term + 0.2 * poly_term + 0.1 * cross_term + 0.1 * barrier