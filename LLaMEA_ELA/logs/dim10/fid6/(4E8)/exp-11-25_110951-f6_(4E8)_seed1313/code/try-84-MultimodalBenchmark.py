import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal radial component with multiple nested oscillations and increased frequency
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 1.5 * np.sin(20 * np.pi * r) * np.cos(10 * np.pi * r) * np.exp(-r**4)
        
        # Multi-modal cosine landscape with chaotic frequency components, phase shifts and enhanced nonlinearity
        cos_term = np.sum(np.cos(9 * np.pi * x_normalized) * np.sin(7 * np.pi * x_normalized) * 
                         np.exp(-0.2 * (x_normalized**2)) * np.sin(3 * np.pi * r))
        
        # Adaptive conditioning with enhanced nonlinearity and dimensionality scaling
        condition_factor = 2.0 + 0.4 * (self.dim - 1) + 0.15 * np.sin(0.8 * self.dim) + 0.12 * np.cos(0.4 * self.dim)
        
        # Higher-order polynomial interaction terms with chaotic perturbations, mixed frequencies and increased complexity
        poly_term = 0.08 * np.sum((x_normalized**10) * np.cos(9 * np.pi * x_normalized) * 
                                 np.sin(4 * np.pi * x_normalized) * np.exp(-0.15 * (x_normalized**2)))
        
        # Cross-dimensional interaction with enhanced chaotic coupling, fractal structure and increased sensitivity
        cross_term = 1.0 * np.sum(np.sin(5 * np.pi * x_normalized[:-1]) * np.cos(5 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.2 * np.abs(x_normalized[:-1] - x_normalized[1:])) * 
                                 np.sin(6 * np.pi * r))
        
        # Modified fractal basin term with increased chaotic frequency components, altered scaling and enhanced complexity
        basin_term = 0.3 * np.sum(np.sin(20 * x_normalized) * np.cos(15 * x_normalized) * 
                                 (1.0 + 0.6 * np.sin(5 * np.pi * r)) * np.exp(-0.3 * r**2))
        
        # Additional chaotic perturbation term with increased complexity, sensitivity and altered frequency components
        chaos_term = 0.15 * np.sum(np.sin(12 * np.pi * x_normalized) * np.cos(9 * np.pi * x_normalized) * 
                                np.exp(-0.4 * (x_normalized**2)) * np.sin(7 * np.pi * r))
        
        # Combine all terms with enhanced conditioning and complexity
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term + chaos_term)