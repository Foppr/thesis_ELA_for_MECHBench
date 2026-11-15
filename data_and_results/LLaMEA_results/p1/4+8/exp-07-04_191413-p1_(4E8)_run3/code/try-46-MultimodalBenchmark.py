import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic_sine = np.sum(np.sin(10 * np.pi * x_scaled) * np.sin(15 * np.pi * x_scaled) * 
                             np.exp(-0.5 * x_scaled**2) + 
                             0.5 * np.sin(20 * np.pi * x_scaled) * np.sin(25 * np.pi * x_scaled) * 
                             np.exp(-0.3 * x_scaled**2) + 
                             0.3 * np.sin(30 * np.pi * x_scaled) * np.sin(35 * np.pi * x_scaled) * 
                             np.exp(-0.1 * x_scaled**2))
        
        # Additional cosine peaks with varying frequencies and amplitudes
        cos_peaks = np.sum(np.cos(8 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                          0.6 * np.cos(16 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2) + 
                          0.4 * np.cos(24 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Cross-dimensional interaction terms with chaotic coupling
        cross_interaction = np.sum(np.sin(np.pi * (x_scaled[:-1] + x_scaled[1:]))**2 * 
                                 np.cos(np.pi * (x_scaled[:-1] - x_scaled[1:]))**2)
        
        # Radial symmetry terms with adaptive conditioning
        radial_symmetry = np.sum(np.exp(-0.5 * (x_scaled**2).sum()) * 
                                np.cos(3 * np.pi * (x_scaled**2).sum()) * 
                                np.sin(4 * np.pi * (x_scaled**2).sum()))
        
        # Adaptive conditioning based on dimensionality
        adaptive_conditioning = np.sum(np.abs(x_scaled)**(1 + 0.1 * self.dim) * 
                                     np.exp(-0.2 * x_scaled**2))
        
        # Combine with different weights
        return quadratic + 0.8 * chaotic_sine + 0.5 * cos_peaks + 0.3 * cross_interaction + 0.2 * radial_symmetry + 0.1 * adaptive_conditioning