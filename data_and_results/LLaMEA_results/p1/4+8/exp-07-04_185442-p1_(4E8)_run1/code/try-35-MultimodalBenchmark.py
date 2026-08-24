import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term with adaptive scaling
        quadratic = np.sum(x_norm**2)
        
        # Enhanced sinusoidal components with varying frequencies and amplitudes
        sin1 = np.sum(np.sin(3 * np.pi * x_norm) ** 2)
        sin2 = np.sum(np.sin(6 * np.pi * x_norm) ** 2)
        sin3 = 0.3 * np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Additional cubic polynomial cross-terms for increased complexity
        poly_cross = 0.4 * np.sum(x_norm**3 * np.sin(4 * np.pi * x_norm))
        
        # Modified interaction terms between dimensions
        interaction = 0.3 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2 * np.cos(3 * np.pi * x_norm[:-1]))
        
        # Add a small random perturbation for landscape diversity
        noise = 0.01 * np.random.random()
        
        # Combine all terms
        return quadratic + sin1 + sin2 + sin3 + poly_cross + interaction + noise