import numpy as np

class ChaoticNestedAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested chaotic attractor structure with varying scales
        nested_chaos = np.sum(np.sin(10 * np.pi * x_norm) * 
                             np.cos(15 * np.pi * x_norm) * 
                             np.exp(-0.5 * np.abs(x_norm)) * 
                             (1 + 0.3 * np.sin(20 * x_norm)))
        
        # Asymmetric basin structure with skewed valleys
        asymmetric_valleys = np.sum(np.abs(x_norm)**1.7 * 
                                  (1 + 0.4 * np.cos(8 * x_norm)) * 
                                  np.exp(-0.2 * x_norm**2) * 
                                  (1 + 0.25 * np.sin(12 * x_norm)))
        
        # Fractional Brownian motion inspired correlation
        fbm_corr = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(0.3 + 0.2 * np.sin(5 * x_norm[:-1])) * 
                         (1 + 0.1 * np.cos(3 * x_norm[:-1])) * 
                         np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])**2))
        
        # Multi-scale harmonic interference
        harmonic_interference = np.sum(np.sin(7 * x_norm) * 
                                     np.cos(9 * x_norm) * 
                                     (1 + 0.3 * np.sin(4 * x_norm)) * 
                                     (1 + 0.2 * np.cos(6 * x_norm)) * 
                                     np.exp(-0.3 * np.abs(x_norm)))
        
        # Non-monotonic gradient regions with local minima
        non_monotonic = np.sum((x_norm**2 + 0.1 * np.sin(25 * x_norm)) * 
                              (1 + 0.2 * np.cos(10 * x_norm)) * 
                              np.exp(-0.4 * x_norm**2))
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_coupling = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                               (1 + 0.3 * np.sin(3 * x_norm[:-1])) * 
                               (1 + 0.2 * np.cos(4 * x_norm[1:])) * 
                               np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])**0.5))
        
        # Combined chaotic landscape with nested complexity
        return 2.0 * (nested_chaos + asymmetric_valleys + fbm_corr + 
                     harmonic_interference + non_monotonic + cross_coupling)