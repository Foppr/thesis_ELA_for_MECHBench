import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like gradient modulation using recursive sine-cosine combinations
        fractal_term = np.sum(np.sin(2 * np.pi * x_norm) * 
                             np.cos(3 * np.pi * x_norm) * 
                             np.sin(5 * np.pi * x_norm) * 
                             np.exp(-0.1 * np.abs(x_norm)))
        
        # Time-variant harmonic components with dynamic frequency coupling
        time_variant = np.sum((np.sin(4 * np.pi * x_norm + 0.5 * np.sin(2 * np.pi * x_norm))) * 
                             (1 + 0.3 * np.cos(6 * np.pi * x_norm)) * 
                             np.exp(-0.3 * x_norm**2))
        
        # Embedded chaotic saddle points with logistic map modulation
        chaotic_saddle = np.sum((x_norm**3 - 0.5 * x_norm**2 + 0.1 * x_norm) * 
                               np.sin(7 * np.pi * x_norm) * 
                               (1 + 0.2 * np.sin(4 * np.pi * x_norm)) * 
                               np.exp(-0.2 * np.abs(x_norm)))
        
        # Self-similar polynomial coupling with multi-scale interactions
        multiscale = np.sum((x_norm**5 + 0.4 * x_norm**3 - 0.2 * x_norm) * 
                           np.cos(3 * x_norm) * 
                           np.exp(-0.1 * x_norm**2))
        
        # Dynamic repulsion field with fractal dimensionality
        dynamic_repulsion = np.sum(1 / (1 + np.exp(-10 * (x_norm**2 - 0.1))) * 
                                  np.sin(5 * x_norm) * 
                                  np.cos(4 * x_norm) * 
                                  np.exp(-0.15 * np.abs(x_norm)))
        
        # Cross-dimensional coupling with recursive interaction terms
        cross_coupling = 0.3 * np.sum((x_norm[:-1] - x_norm[1:])**2 * 
                                    np.sin(2 * (x_norm[:-1] + x_norm[1:])) * 
                                    np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Global conditioning with logarithmic and exponential scaling
        global_conditioning = 0.2 * np.sum(np.log(1 + np.abs(x_norm)) * np.exp(-0.1 * x_norm**2))
        
        # Combine all terms
        return fractal_term + time_variant - chaotic_saddle + multiscale + dynamic_repulsion + cross_coupling + global_conditioning