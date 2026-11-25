import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal modulation with chaotic phase shifts
        chaotic_modulation = np.sum(np.sin(10 * x_norm + np.sin(7 * x_norm)) * 
                                   np.cos(8 * x_norm + np.cos(5 * x_norm)))
        
        # Polynomial basin structure with varying degrees
        polynomial_basins = np.sum(x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2 + 
                                  0.1 * x_norm + 0.05 * np.sin(3 * x_norm))
        
        # Radial symmetry with adaptive scaling
        radial_symmetry = np.sum(np.exp(-0.5 * (x_norm**2)) * 
                                (1 + 0.3 * np.cos(4 * np.sqrt(np.sum(x_norm**2)))))
        
        # Cross-dimensional interaction with hyperbolic scaling
        cross_dim_interaction = np.sum((np.abs(x_norm[:-1]) + np.abs(x_norm[1:])) * 
                                     np.tanh(x_norm[:-1] * x_norm[1:]) * 
                                     (1 + 0.2 * np.sin(6 * x_norm[:-1])))
        
        # Multi-scale chaotic oscillation
        multi_scale_oscillation = np.sum(np.sin(15 * x_norm) * 
                                        np.cos(12 * x_norm) * 
                                        np.exp(-0.1 * np.abs(x_norm)) * 
                                        (1 + 0.1 * np.sin(9 * x_norm)))
        
        # Adaptive conditioning with exponential scaling
        adaptive_conditioning = np.sum(np.exp(0.5 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(3 * x_norm)) * 
                                     (1 + 0.3 * np.sin(7 * x_norm)))
        
        # Combined landscape with varying curvature and basin complexity
        return 2.0 * (chaotic_modulation + polynomial_basins + radial_symmetry + 
                     cross_dim_interaction + multi_scale_oscillation + adaptive_conditioning)