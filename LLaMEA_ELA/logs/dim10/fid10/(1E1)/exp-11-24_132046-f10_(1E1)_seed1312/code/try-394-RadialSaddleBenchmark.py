import numpy as np

class RadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple basins
        radial_term = np.sum((x_norm**2 + 0.5 * np.sin(4 * np.pi * x_norm)**2) * 
                            (1 + 0.3 * np.cos(6 * np.pi * x_norm)))
        
        # Sinusoidal oscillations creating multimodal structure
        oscillation_term = np.sum(np.sin(8 * np.pi * x_norm) * 
                                 np.cos(5 * np.pi * x_norm) * 
                                 (1 + 0.2 * np.sin(3 * np.pi * x_norm)))
        
        # Asymmetric saddle points with varying curvature
        saddle_term = np.sum((x_norm**4 - 2 * x_norm**2 + 0.5) * 
                            (1 + 0.4 * np.cos(7 * np.pi * x_norm)) * 
                            (1 + 0.3 * np.sin(9 * np.pi * x_norm)))
        
        # Cross-dimensional interaction with directional bias
        cross_term = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                           (1 + 0.2 * np.sin(5 * np.pi * x_norm[:-1])) * 
                           (1 + 0.1 * np.cos(3 * np.pi * x_norm[1:])))
        
        # Power-law conditioned regions with non-uniform scaling
        power_term = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(10 * np.pi * x_norm)))
        
        # Combined landscape with varying difficulty regions
        return 2.0 * (radial_term + oscillation_term + saddle_term + cross_term + power_term)