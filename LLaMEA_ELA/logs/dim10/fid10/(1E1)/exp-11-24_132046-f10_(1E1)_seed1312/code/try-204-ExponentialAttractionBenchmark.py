import numpy as np

class ExponentialAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential repulsion fields centered at regular grid points
        repulsion_fields = np.sum(np.exp(-np.sum((x_norm[:, None] - np.linspace(-1, 1, self.dim)[None, :])**2, axis=0) / 0.1))
        
        # Polynomial attraction wells with varying degrees
        attraction_wells = np.sum(0.5 * x_norm**4 + 0.3 * x_norm**3 + 0.2 * x_norm**2)
        
        # Fractal dimensionality scaling with recursive self-similarity
        fractal_scaling = 0.0
        for i in range(1, min(5, self.dim + 1)):
            if self.dim >= i:
                fractal_scaling += np.sum(np.sin(x_norm * (2**i)) * np.cos(x_norm * (3**i)) * (1 + 0.1 * np.sin(x_norm * (5**i))))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.5 + 0.5 * np.cos(3 * x_norm[:-1]))))
        
        # Multi-scale harmonic modulation with varying frequencies
        harmonic_modulation = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                                    (1 + 0.3 * np.sin(5 * np.pi * x_norm)) * 
                                    (1 + 0.2 * np.cos(7 * np.pi * x_norm)))
        
        # Power-law conditioned regions with varying exponents
        power_law_regions = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(4 * x_norm)))
        
        # Adaptive conditioning with local scaling based on distance to center
        adaptive_conditioning = np.sum((1 + 0.3 * np.sin(2 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2) * 
                                     (1 + 0.2 * np.cos(3 * x_norm)))
        
        # Combined landscape with different curvature regions
        return 2.0 * (repulsion_fields + attraction_wells + fractal_scaling + 
                     cross_coupling + harmonic_modulation + power_law_regions + 
                     adaptive_conditioning)