import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_normalized**2))
        radial_term = 0.5 * np.sin(5 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape
        cos_term = np.sum(np.cos(2 * np.pi * x_normalized) * np.exp(-0.5 * (x_normalized**2)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * (self.dim - 1)
        
        # Polynomial interaction terms
        poly_term = 0.01 * np.sum((x_normalized**4) * np.cos(3 * np.pi * x_normalized))
        
        # Cross-dimensional interaction
        cross_term = 0.3 * np.sum(np.sin(np.pi * x_normalized[:-1]) * np.cos(np.pi * x_normalized[1:]))
        
        # Combine all terms with adaptive scaling
        return condition_factor * (radial_term + cos_term + poly_term + cross_term)