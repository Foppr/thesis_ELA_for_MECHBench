import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal radial component with multiple nested oscillations and self-similarity
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 1.2 * np.sin(12 * np.pi * r) * np.cos(6 * np.pi * r) * np.exp(-r**3)
        
        # Intensified multi-modal cosine landscape with chaotic frequency components and increased nonlinearity
        cos_term = np.sum(np.cos(7 * np.pi * x_normalized) * np.sin(5 * np.pi * x_normalized) * 
                         np.exp(-0.3 * (x_normalized**2)) * np.sin(4 * np.pi * r))
        
        # Enhanced adaptive conditioning with exponential complexity and dimensionality scaling
        condition_factor = 1.0 + 0.3 * (self.dim - 1) + 0.1 * np.sin(0.7 * self.dim) + 0.02 * r**2
        
        # Higher-order polynomial interaction terms with stronger chaotic perturbations and multi-scale effects
        poly_term = 0.05 * np.sum((x_normalized**8) * np.cos(7 * np.pi * x_normalized) * 
                                 np.sin(3 * np.pi * x_normalized) * np.exp(-0.1 * r**2))
        
        # Enhanced cross-dimensional interaction with stronger chaotic sine-cosine coupling and fractal structure
        cross_term = 0.7 * np.sum(np.sin(3 * np.pi * x_normalized[:-1]) * np.cos(3 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.2 * np.abs(x_normalized[:-1] - x_normalized[1:])) * 
                                 np.sin(2 * np.pi * r))
        
        # Augmented fractal perturbation term with enhanced basin-like characteristics and multi-scale structure
        basin_term = 0.2 * np.sum(np.sin(11 * x_normalized) * np.cos(11 * x_normalized) * 
                                 (1.0 + 0.5 * np.sin(4 * np.pi * r)) * np.exp(-0.1 * r**2))
        
        # Additional chaotic coupling term with increased complexity and multi-modal interference
        chaos_term = 0.1 * np.sum(np.sin(10 * x_normalized) * np.cos(8 * x_normalized) * 
                                 np.sin(6 * np.pi * r) * np.cos(3 * np.pi * r))
        
        # Combine all terms with enhanced scaling and extreme conditioning
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term + chaos_term)