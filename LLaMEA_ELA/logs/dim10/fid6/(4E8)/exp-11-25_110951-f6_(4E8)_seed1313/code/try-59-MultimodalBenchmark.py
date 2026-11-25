import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal-like radial component with multiple nested peaks and chaotic modulation
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 0.9 * np.sin(10 * np.pi * r) * np.cos(5 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape with altered frequencies, chaotic modulation, and adaptive scaling
        cos_term = np.sum(np.cos(5 * np.pi * x_normalized) * np.sin(4 * np.pi * x_normalized) * 
                         np.exp(-0.3 * (x_normalized**2)))
        
        # Adaptive conditioning based on dimensionality with increased complexity and chaotic perturbation
        condition_factor = 1.0 + 0.3 * (self.dim - 1) + 0.05 * np.sin(7 * np.pi * r)
        
        # Enhanced polynomial interaction terms with higher order, fractal-like structure, and multi-scale modulation
        poly_term = 0.04 * np.sum((x_normalized**7) * np.cos(6 * np.pi * x_normalized) * 
                                np.exp(-0.1 * (x_normalized**2)))
        
        # Cross-dimensional interaction with enhanced chaotic sine-cosine coupling, fractal modulation, and multi-scale coupling
        cross_term = 0.6 * np.sum(np.sin(3 * np.pi * x_normalized[:-1]) * np.cos(3 * np.pi * x_normalized[1:]) * 
                                (1 + 0.15 * np.sin(7 * np.pi * x_normalized[:-1])) * 
                                np.exp(-0.2 * (x_normalized[:-1]**2) - 0.2 * (x_normalized[1:]**2)))
        
        # Additional enhanced chaotic perturbation term with fractal-like structure and multi-scale frequency components
        chaos_term = 0.2 * np.sum(np.sin(11 * x_normalized) * np.cos(11 * x_normalized) * 
                                 np.exp(-0.4 * (x_normalized**2)) * 
                                 np.sin(8 * np.pi * r))
        
        # Novel enhanced fractal-like basin term with multiple basins and complex landscape structure
        basin_term = 0.35 * np.prod(np.cos(3 * np.pi * x_normalized)) * np.exp(-0.15 * r**2) + \
                     0.1 * np.sin(12 * np.pi * r) * np.cos(6 * np.pi * r)
        
        # Combine all terms with adaptive scaling and enhanced chaotic modulation
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + chaos_term + basin_term)