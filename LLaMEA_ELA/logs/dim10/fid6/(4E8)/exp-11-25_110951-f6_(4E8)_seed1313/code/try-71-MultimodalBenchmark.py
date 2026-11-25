import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal radial component with multiple nested oscillations
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 1.2 * np.sin(12 * np.pi * r) * np.cos(6 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape with chaotic frequency components and phase shifts
        cos_term = np.sum(np.cos(7 * np.pi * x_normalized) * np.sin(5 * np.pi * x_normalized) * 
                         np.exp(-0.3 * (x_normalized**2)) * np.sin(2 * np.pi * r))
        
        # Adaptive conditioning with increased nonlinearity and dimensionality effects
        condition_factor = 1.5 + 0.3 * (self.dim - 1) + 0.1 * np.sin(0.8 * self.dim) + 0.08 * np.cos(0.3 * self.dim)
        
        # Higher-order polynomial interaction with enhanced chaotic perturbations
        poly_term = 0.05 * np.sum((x_normalized**8) * np.cos(7 * np.pi * x_normalized) * 
                                 np.sin(3 * np.pi * x_normalized) * np.exp(-0.1 * (x_normalized**2)))
        
        # Cross-dimensional interaction with complex sine-cosine coupling and fractal structure
        cross_term = 0.7 * np.sum(np.sin(3 * np.pi * x_normalized[:-1]) * np.cos(3 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.2 * np.abs(x_normalized[:-1] - x_normalized[1:])) * 
                                 np.sin(4 * np.pi * r))
        
        # Modified basin term with enhanced fractal characteristics and chaotic perturbations
        basin_term = 0.2 * np.sum(np.sin(15 * x_normalized) * np.cos(12 * x_normalized) * 
                                 (1.0 + 0.4 * np.sin(5 * np.pi * r)) * np.exp(-0.1 * r**2))
        
        # Additional chaotic perturbation with multi-scale frequency components
        chaos_term = 0.1 * np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(8 * np.pi * x_normalized) * 
                                 np.sin(6 * np.pi * r) * np.cos(4 * np.pi * r))
        
        # Combine all terms with adaptive scaling and enhanced conditioning
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term + chaos_term)