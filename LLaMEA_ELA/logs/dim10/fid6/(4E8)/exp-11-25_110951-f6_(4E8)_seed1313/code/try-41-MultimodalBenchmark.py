import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_normalized**2))
        radial_term = 0.7 * np.sin(6 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape with altered frequencies
        cos_term = np.sum(np.cos(3 * np.pi * x_normalized) * np.exp(-0.3 * (x_normalized**2)))
        
        # Adaptive conditioning based on dimensionality with increased complexity
        condition_factor = 1.0 + 0.15 * (self.dim - 1)
        
        # Polynomial interaction terms with higher order
        poly_term = 0.02 * np.sum((x_normalized**5) * np.cos(4 * np.pi * x_normalized))
        
        # Cross-dimensional interaction with chaotic sine-cosine coupling
        cross_term = 0.4 * np.sum(np.sin(1.5 * np.pi * x_normalized[:-1]) * np.cos(1.5 * np.pi * x_normalized[1:]))
        
        # Additional chaotic perturbation term
        chaos_term = 0.1 * np.sum(np.sin(7 * x_normalized) * np.cos(7 * x_normalized))
        
        # Combine all terms with adaptive scaling
        return condition_factor * (radial_term + cos_term + poly_term + cross_term + chaos_term)