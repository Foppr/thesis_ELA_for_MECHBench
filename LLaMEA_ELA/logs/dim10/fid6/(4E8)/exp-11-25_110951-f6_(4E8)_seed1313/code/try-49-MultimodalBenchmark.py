import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with multiple peaks and fractal-like structure
        r = np.sqrt(np.sum(x_normalized**2))
        radial_term = 0.8 * np.sin(7 * np.pi * r) * np.exp(-r**2) + 0.2 * np.sin(15 * np.pi * r) * np.exp(-(r**2)/2)
        
        # Multi-modal cosine landscape with altered frequencies and chaotic perturbations
        cos_term = np.sum(np.cos(4 * np.pi * x_normalized) * np.exp(-0.25 * (x_normalized**2)) + 
                         0.1 * np.sin(9 * x_normalized) * np.cos(9 * x_normalized))
        
        # Adaptive conditioning based on dimensionality with increased complexity
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        
        # Polynomial interaction terms with higher order and additional chaotic components
        poly_term = 0.03 * np.sum((x_normalized**6) * np.cos(5 * np.pi * x_normalized) + 
                                0.05 * np.sin(8 * x_normalized) * np.cos(8 * x_normalized))
        
        # Cross-dimensional interaction with enhanced chaotic sine-cosine coupling
        cross_term = 0.5 * np.sum(np.sin(2 * np.pi * x_normalized[:-1]) * np.cos(2 * np.pi * x_normalized[1:]) + 
                                0.1 * np.sin(6 * x_normalized[:-1]) * np.cos(6 * x_normalized[1:]))
        
        # Additional fractal-like basin term to create complex terrain
        basin_term = 0.3 * np.sum(np.exp(-5 * (x_normalized**2)) * np.sin(10 * np.pi * x_normalized))
        
        # Combine all terms with adaptive scaling
        return condition_factor * (radial_term + cos_term + poly_term + cross_term + basin_term)