import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal-like radial component with improved scaling and complexity
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 0.8 * np.sin(12 * np.pi * r) * np.cos(6 * np.pi * r) * np.exp(-r**2)
        
        # Modified multi-modal cosine landscape with adjusted frequency components
        cos_term = np.sum(np.cos(7 * np.pi * x_normalized) * np.sin(5 * np.pi * x_normalized) * np.exp(-0.3 * (x_normalized**2)))
        
        # Enhanced adaptive conditioning with improved dimensionality impact
        condition_factor = 1.0 + 0.3 * (self.dim - 1) + 0.08 * np.sin(0.7 * self.dim)
        
        # Modified higher-order polynomial interaction terms with refined chaotic perturbations
        poly_term = 0.05 * np.sum((x_normalized**8) * np.cos(7 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized))
        
        # Improved cross-dimensional interaction with enhanced chaotic sine-cosine coupling
        cross_term = 0.7 * np.sum(np.sin(3 * np.pi * x_normalized[:-1]) * np.cos(3 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.15 * np.abs(x_normalized[:-1] - x_normalized[1:])))
        
        # Refined fractal perturbation term with shifted basin characteristics and improved sensitivity
        basin_term = 0.25 * np.sum(np.sin(12 * x_normalized) * np.cos(12 * x_normalized) * 
                                   (1.0 + 0.4 * np.sin(4 * np.pi * r)))
        
        # Combine all terms with optimized scaling and enhanced conditioning
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term)