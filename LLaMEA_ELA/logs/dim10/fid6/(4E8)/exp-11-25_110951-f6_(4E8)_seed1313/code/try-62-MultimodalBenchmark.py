import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like radial component with modified scaling and increased complexity
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 0.9 * np.sin(10 * np.pi * r) * np.cos(5 * np.pi * r) * np.exp(-r**2)
        
        # Multi-modal cosine landscape with altered frequency components
        cos_term = np.sum(np.cos(6 * np.pi * x_normalized) * np.sin(4 * np.pi * x_normalized) * np.exp(-0.25 * (x_normalized**2)))
        
        # Adaptive conditioning with modified dimensionality impact
        condition_factor = 1.0 + 0.25 * (self.dim - 1) + 0.06 * np.sin(0.6 * self.dim)
        
        # Higher-order polynomial interaction terms with modified chaotic perturbations
        poly_term = 0.04 * np.sum((x_normalized**7) * np.cos(6 * np.pi * x_normalized) * np.sin(2.5 * np.pi * x_normalized))
        
        # Cross-dimensional interaction with modified chaotic sine-cosine coupling
        cross_term = 0.6 * np.sum(np.sin(2.5 * np.pi * x_normalized[:-1]) * np.cos(2.5 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.12 * np.abs(x_normalized[:-1] - x_normalized[1:])))
        
        # Modified fractal perturbation term with shifted basin characteristics
        basin_term = 0.2 * np.sum(np.sin(10 * x_normalized) * np.cos(10 * x_normalized) * 
                                  (1.0 + 0.35 * np.sin(3.5 * np.pi * r)))
        
        # Combine all terms with modified scaling and enhanced conditioning
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term)