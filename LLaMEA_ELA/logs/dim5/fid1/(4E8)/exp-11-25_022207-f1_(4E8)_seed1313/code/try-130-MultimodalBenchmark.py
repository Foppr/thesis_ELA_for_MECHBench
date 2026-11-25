import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic modulation with logistic map and sine coupling
        chaotic_modulation = np.sum(np.sin(3 * np.pi * x_norm) * 
                                   np.cos(5 * np.pi * x_norm) * 
                                   (1 + 0.3 * np.sin(7 * np.pi * x_norm)) * 
                                   np.exp(-0.2 * np.abs(x_norm)))
        
        # Periodic attractor basins with exponential coupling
        periodic_attractors = np.sum((np.sin(2 * np.pi * x_norm)**2 + 
                                     0.5 * np.cos(4 * np.pi * x_norm)**2) * 
                                    np.exp(-0.1 * x_norm**2))
        
        # Saddle-point repulsion with asymmetric harmonic components
        saddle_repulsion = np.sum((x_norm**3 - 0.3 * x_norm**2 + 0.05 * x_norm) * 
                                 np.sin(6 * np.pi * x_norm) * 
                                 (1 + 0.25 * np.cos(8 * np.pi * x_norm)) * 
                                 np.exp(-0.15 * np.abs(x_norm)))
        
        # Multi-scale fractal interactions with polynomial coupling
        fractal_coupling = np.sum((x_norm**4 + 0.3 * x_norm**2 - 0.1 * x_norm) * 
                                 np.cos(2 * x_norm) * 
                                 np.exp(-0.2 * x_norm**2))
        
        # Dynamic repulsion field with recursive exponential terms
        dynamic_repulsion = np.sum(np.exp(-5 * (x_norm**2 - 0.05)) * 
                                  np.sin(4 * x_norm) * 
                                  np.cos(3 * x_norm) * 
                                  np.exp(-0.1 * np.abs(x_norm)))
        
        # Cross-dimensional coupling with asymmetric interaction terms
        cross_coupling = 0.25 * np.sum((x_norm[:-1] - x_norm[1:])**2 * 
                                     np.sin(3 * (x_norm[:-1] + x_norm[1:])) * 
                                     np.exp(-0.15 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Global conditioning with multi-modal exponential scaling
        global_conditioning = 0.15 * np.sum(np.exp(-0.1 * np.abs(x_norm)) * 
                                          np.sin(3 * x_norm) * 
                                          np.cos(2 * x_norm))
        
        # Additional non-separable complexity through trigonometric interactions
        non_separable = 0.2 * np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                   np.cos(np.pi * (x_norm[:-1] * x_norm[1:])) * 
                                   np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Combine all terms
        return chaotic_modulation + periodic_attractors - saddle_repulsion + fractal_coupling + dynamic_repulsion + cross_coupling + global_conditioning + non_separable