import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like radial component with multiple nested peaks
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 0.8 * np.sin(8 * np.pi * r) * np.cos(4 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape with altered frequencies and chaotic modulation
        cos_term = np.sum(np.cos(4 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized) * np.exp(-0.25 * (x_normalized**2)))
        
        # Adaptive conditioning based on dimensionality with increased complexity
        condition_factor = 1.0 + 0.2 * (self.dim - 1)
        
        # Polynomial interaction terms with higher order and fractal-like structure
        poly_term = 0.03 * np.sum((x_normalized**6) * np.cos(5 * np.pi * x_normalized))
        
        # Cross-dimensional interaction with chaotic sine-cosine coupling and fractal modulation
        cross_term = 0.5 * np.sum(np.sin(2 * np.pi * x_normalized[:-1]) * np.cos(2 * np.pi * x_normalized[1:]) * 
                                (1 + 0.1 * np.sin(6 * np.pi * x_normalized[:-1])))
        
        # Additional chaotic perturbation term with fractal-like structure
        chaos_term = 0.15 * np.sum(np.sin(9 * x_normalized) * np.cos(9 * x_normalized) * 
                                 np.exp(-0.5 * (x_normalized**2)))
        
        # Novel fractal-like basin term to create complex landscape with multiple basins
        basin_term = 0.3 * np.prod(np.cos(2.5 * np.pi * x_normalized)) * np.exp(-0.1 * r**2)
        
        # Combine all terms with adaptive scaling
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + chaos_term + basin_term)