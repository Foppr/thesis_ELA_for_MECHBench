import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested chaotic attractor structure with multiple local minima
        chaotic_terms = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) + 
                              np.sin(15 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm))
        
        # Asymmetric basin structure with varying curvature
        asymmetric_basins = np.sum(np.abs(x_norm)**1.7 * (1 + 0.3 * np.sin(5 * np.pi * x_norm)) * 
                                  (1 + 0.4 * np.cos(7 * np.pi * x_norm)))
        
        # Scale-invariant ruggedness with multi-scale peaks
        ruggedness = np.sum(np.exp(-np.abs(x_norm)**2.5) * 
                           (1 + 0.5 * np.sin(3 * np.pi * x_norm)) * 
                           (1 + 0.3 * np.cos(6 * np.pi * x_norm)))
        
        # Non-monotonic behavior with oscillating conditioning
        non_monotonic = np.sum(np.sin(2 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2) * 
                              (1 + 0.2 * np.sin(4 * np.pi * x_norm)) * 
                              (1 + 0.1 * np.cos(8 * np.pi * x_norm)))
        
        # Multi-scale harmonic interference
        harmonic_interference = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                                     (1 + 0.25 * np.sin(2 * np.pi * x_norm)) * 
                                     (1 + 0.3 * np.cos(3 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with varying strength
        cross_coupling = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.2 * np.sin(3 * np.pi * x_norm[:-1])) * 
                               (1 + 0.15 * np.cos(4 * np.pi * x_norm[1:])))
        
        # Fractal-like conditioning with irregular scaling
        fractal_conditioning = np.sum(np.exp(-np.abs(x_norm)**1.8) * 
                                    (1 + 0.3 * np.sin(9 * np.pi * x_norm)) * 
                                    (1 + 0.25 * np.cos(11 * np.pi * x_norm)))
        
        # Combined landscape with mixed curvature regions
        return 2.0 * (chaotic_terms + asymmetric_basins + ruggedness + 
                     non_monotonic + harmonic_interference + cross_coupling + 
                     fractal_conditioning)