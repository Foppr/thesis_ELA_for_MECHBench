import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like radial component with multiple peaks and self-similarity
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 0.8 * np.sin(8 * np.pi * r) * np.cos(4 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape with enhanced chaotic frequency components
        cos_term = np.sum(np.cos(5 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized) * np.exp(-0.2 * (x_normalized**2)))
        
        # Adaptive conditioning based on dimensionality with increased complexity and nonlinearity
        condition_factor = 1.0 + 0.2 * (self.dim - 1) + 0.05 * np.sin(0.5 * self.dim)
        
        # Higher-order polynomial interaction terms with chaotic perturbations
        poly_term = 0.03 * np.sum((x_normalized**6) * np.cos(5 * np.pi * x_normalized) * np.sin(2 * np.pi * x_normalized))
        
        # Cross-dimensional interaction with enhanced chaotic sine-cosine coupling and fractal structure
        cross_term = 0.5 * np.sum(np.sin(2 * np.pi * x_normalized[:-1]) * np.cos(2 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.1 * np.abs(x_normalized[:-1] - x_normalized[1:])))
        
        # Additional fractal perturbation term with basin-like characteristics
        basin_term = 0.15 * np.sum(np.sin(9 * x_normalized) * np.cos(9 * x_normalized) * 
                                  (1.0 + 0.3 * np.sin(3 * np.pi * r)))
        
        # Combine all terms with adaptive scaling and enhanced conditioning
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term)