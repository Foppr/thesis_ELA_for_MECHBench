import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basins with sinusoidal modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Multi-scale sinusoidal oscillations
        sinusoidal_oscillations = np.sum(np.sin(2 * np.pi * x_norm) * 
                                       np.cos(3 * np.pi * x_norm) * 
                                       (1 + 0.2 * np.sin(7 * np.pi * x_norm)))
        
        # Cross-dimensional interaction with radial dependence
        cross_dim_interaction = np.sum(np.sin(np.pi * x_norm[:-1] * x_norm[1:]) * 
                                     (1 + 0.1 * np.cos(4 * np.pi * x_norm[:-1])) * 
                                     (1 + 0.1 * np.sin(3 * np.pi * x_norm[1:])))
        
        # Adaptive conditioning based on distance from origin
        adaptive_conditioning = np.sum((1 + 0.5 * np.sin(2 * np.pi * np.sqrt(np.sum(x_norm**2)))) * 
                                     np.exp(-0.5 * (x_norm**2) / (0.3 + 0.2 * np.cos(6 * np.pi * x_norm))))
        
        # Fractal-like structure with varying frequency
        fractal_structure = np.sum(np.sin(15 * np.pi * x_norm) * 
                                 np.exp(-np.abs(x_norm) / (0.1 + 0.1 * np.sin(8 * np.pi * x_norm))))
        
        # Gaussian-like peaks with varying heights and widths
        gaussian_peaks = np.sum(0.5 * np.exp(-0.5 * (x_norm**2) / (0.2 + 0.1 * np.sin(9 * np.pi * x_norm))) * 
                              (1 + 0.3 * np.cos(4 * np.pi * x_norm)))
        
        # Combined landscape
        return 2.0 * (radial_basins + sinusoidal_oscillations + cross_dim_interaction + 
                     adaptive_conditioning + fractal_structure + gaussian_peaks)