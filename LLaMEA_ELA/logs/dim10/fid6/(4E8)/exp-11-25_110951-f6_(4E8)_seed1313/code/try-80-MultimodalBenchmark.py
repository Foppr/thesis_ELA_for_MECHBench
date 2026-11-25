import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal radial component with multiple nested oscillations and higher frequency harmonics
        r = np.sqrt(np.sum(x_normalized**2))
        fractal_radial = 1.5 * np.sin(20 * np.pi * r) * np.cos(10 * np.pi * r) * np.exp(-r**3)
        
        # Multi-modal cosine landscape with chaotic frequency components, phase shifts, and higher-order interactions
        cos_term = np.sum(np.cos(10 * np.pi * x_normalized) * np.sin(8 * np.pi * x_normalized) * 
                         np.exp(-0.5 * (x_normalized**2)) * np.sin(3 * np.pi * r) * np.cos(2 * np.pi * r))
        
        # Adaptive conditioning with increased nonlinearity, dimensionality effects, and chaotic scaling factors
        condition_factor = 2.0 + 0.5 * (self.dim - 1) + 0.2 * np.sin(1.2 * self.dim) + 0.15 * np.cos(0.5 * self.dim) + 0.1 * np.sin(0.3 * self.dim**2)
        
        # Higher-order polynomial interaction with enhanced chaotic perturbations and multi-scale coupling
        poly_term = 0.1 * np.sum((x_normalized**10) * np.cos(9 * np.pi * x_normalized) * 
                                np.sin(4 * np.pi * x_normalized) * np.exp(-0.2 * (x_normalized**2)))
        
        # Cross-dimensional interaction with complex sine-cosine coupling, fractal structure, and multi-scale chaos
        cross_term = 1.0 * np.sum(np.sin(5 * np.pi * x_normalized[:-1]) * np.cos(5 * np.pi * x_normalized[1:]) * 
                                 np.exp(-0.3 * np.abs(x_normalized[:-1] - x_normalized[1:])) * 
                                 np.sin(6 * np.pi * r) * np.cos(4 * np.pi * r))
        
        # Modified basin term with enhanced fractal characteristics, chaotic perturbations, and multi-scale oscillations
        basin_term = 0.3 * np.sum(np.sin(20 * x_normalized) * np.cos(15 * x_normalized) * 
                                 (1.0 + 0.6 * np.sin(7 * np.pi * r)) * np.exp(-0.2 * r**2) * np.sin(3 * np.pi * r))
        
        # Additional chaotic perturbation with multi-scale frequency components, higher harmonics, and complex coupling
        chaos_term = 0.15 * np.sum(np.sin(15 * np.pi * x_normalized) * np.cos(12 * np.pi * x_normalized) * 
                                  np.sin(8 * np.pi * r) * np.cos(6 * np.pi * r) * np.exp(-0.1 * r))
        
        # Novel cross-dimensional coupling with hyper-chaotic interactions and fractal interference patterns
        hyper_cross_term = 0.25 * np.sum(np.sin(7 * np.pi * x_normalized[:-1]) * np.cos(7 * np.pi * x_normalized[1:]) * 
                                        np.exp(-0.4 * np.abs(x_normalized[:-1] - x_normalized[1:])) * 
                                        np.sin(5 * np.pi * r) * np.cos(3 * np.pi * r) * np.sin(2 * np.pi * x_normalized[:-1]) * np.cos(2 * np.pi * x_normalized[1:]))
        
        # Combine all terms with adaptive scaling, enhanced conditioning, and novel interaction patterns
        return condition_factor * (fractal_radial + cos_term + poly_term + cross_term + basin_term + chaos_term + hyper_cross_term)