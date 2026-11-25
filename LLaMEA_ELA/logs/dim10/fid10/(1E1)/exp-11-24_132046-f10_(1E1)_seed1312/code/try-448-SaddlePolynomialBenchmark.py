import numpy as np

class SaddlePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial valley structure with multiple local minima
        polynomial_valleys = np.sum(0.5 * x_norm**4 - 2.0 * x_norm**2 + 1.0)
        
        # Saddle point configuration with hyperbolic tangent interactions
        saddle_points = np.sum(np.tanh(x_norm[:-1] * x_norm[1:]) * 
                              (x_norm[:-1]**2 + x_norm[1:]**2) * 
                              (1 + 0.3 * np.sin(3 * np.pi * x_norm[:-1])))
        
        # Radial symmetry with oscillating depth
        radial_symmetry = np.sum(np.exp(-0.5 * np.sum(x_norm**2, axis=0)) * 
                                (1 + 0.4 * np.cos(8 * np.arctan2(x_norm[1], x_norm[0]))))
        
        # Cross-dimensional harmonic coupling with varying frequencies
        harmonic_coupling = np.sum(np.sin(2 * np.pi * x_norm[:-1]) * 
                                  np.cos(3 * np.pi * x_norm[1:]) * 
                                  (1 + 0.2 * np.sin(5 * np.pi * x_norm[:-1])) * 
                                  (1 + 0.1 * np.cos(4 * np.pi * x_norm[1:])))
        
        # Deceptive gradient structure with local perturbations
        deceptive_gradients = np.sum(0.3 * np.sin(15 * x_norm) * 
                                   np.exp(-0.1 * x_norm**2) * 
                                   (1 + 0.2 * np.cos(7 * x_norm)))
        
        # Multi-scale conditioning with exponential modulation
        multi_scale_conditioning = np.sum(np.exp(0.5 * x_norm) * 
                                         (1 + 0.3 * np.sin(6 * x_norm)) * 
                                         (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Combined landscape with mixed curvature regions
        return 2.0 * (polynomial_valleys + saddle_points + radial_symmetry + 
                     harmonic_coupling + deceptive_gradients + multi_scale_conditioning)