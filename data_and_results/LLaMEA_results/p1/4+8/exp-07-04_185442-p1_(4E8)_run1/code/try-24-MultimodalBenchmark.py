import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with varying frequencies and powers
        sin1 = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        sin2 = np.sum(np.sin(10 * np.pi * x_norm) ** 3)
        sin3 = np.sum(np.sin(15 * np.pi * x_norm) ** 4)
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.05 * np.sum(np.sin(np.pi * x_norm * (1 + np.sin(2 * np.pi * x_norm))) ** 2)
        
        # Polynomial interaction terms with mixed degrees
        poly2 = 0.1 * np.sum(x_norm**4)
        poly3 = 0.05 * np.sum(x_norm**6)
        
        # Cross-terms to increase dimensionality coupling
        cross = 0.2 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * x_norm[:-1]))
        
        # Combine all terms
        return quadratic + 0.5 * sin1 + 0.3 * sin2 + 0.2 * sin3 + chaotic + poly2 + poly3 + cross