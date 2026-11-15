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
        sin1 = np.sum(np.sin(2 * np.pi * x_norm) ** 2)
        sin2 = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        sin3 = 0.5 * np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        sin4 = 0.3 * np.sum(np.sin(12 * np.pi * x_norm) ** 2)
        
        # Higher-order polynomial cross-terms for increased complexity
        poly_cross = 0.3 * np.sum(x_norm**3 * np.sin(3 * np.pi * x_norm))
        poly_cross += 0.2 * np.sum(x_norm**4 * np.cos(4 * np.pi * x_norm))
        
        # Interaction terms between dimensions with non-linear coupling
        interaction = 0.2 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2 * np.cos(2 * np.pi * x_norm[:-1]))
        interaction += 0.1 * np.sum((x_norm[:-2] - x_norm[2:]) ** 2 * np.sin(3 * np.pi * x_norm[:-2]))
        
        # Additional complex landscape features
        complex_term = 0.15 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        complex_term += 0.1 * np.sum(np.exp(-x_norm**2) * np.sin(6 * np.pi * x_norm))
        
        # Add a small random perturbation for landscape diversity
        noise = 0.02 * np.random.random()
        
        # Combine all terms
        return quadratic + sin1 + sin2 + sin3 + sin4 + poly_cross + interaction + complex_term + noise