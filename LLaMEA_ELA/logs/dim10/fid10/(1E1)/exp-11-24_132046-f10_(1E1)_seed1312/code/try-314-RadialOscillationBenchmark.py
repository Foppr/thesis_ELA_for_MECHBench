import numpy as np

class RadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with varying depths
        radial_basins = np.sum((x_norm**2).sum() * (1 + 0.3 * np.sin(5 * np.sqrt(x_norm**2).sum())))
        
        # Multi-scale sinusoidal oscillations
        oscillations = np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm) * 
                             (1 + 0.2 * np.sin(6 * x_norm)) * 
                             (1 + 0.15 * np.cos(4 * x_norm)))
        
        # Cross-dimensional interaction with radial symmetry
        cross_dim_interaction = np.sum(np.sin(np.pi * x_norm[:-1] * x_norm[1:]) * 
                                     np.cos(np.pi * x_norm[:-1] / x_norm[1:]))
        
        # Adaptive conditioning based on distance from origin
        adaptive_conditioning = np.sum((1 + 0.5 * np.sin(3 * np.sqrt(x_norm**2).sum())) * 
                                     np.exp(-0.2 * (x_norm**2).sum()) * 
                                     (1 + 0.2 * np.cos(2 * np.sqrt(x_norm**2).sum())))
        
        # Fractal-like periodicity with varying scales
        fractal_periodicity = np.sum(np.sin(15 * x_norm) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Gaussian-like peaks with dynamic widths
        gaussian_peaks = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.2 * np.cos(7 * x_norm))))
        
        # Combined landscape
        return 1.2 * (radial_basins + oscillations + cross_dim_interaction + 
                     adaptive_conditioning + fractal_periodicity + gaussian_peaks)