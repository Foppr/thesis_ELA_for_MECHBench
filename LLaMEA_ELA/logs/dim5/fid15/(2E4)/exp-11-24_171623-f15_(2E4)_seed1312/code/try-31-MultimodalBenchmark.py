import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay term with radial component and additional frequency modulation
        exp_term = np.sum(np.exp(-0.3 * np.sum(x_norm**2, axis=0)) * 
                         (1.0 + 0.3 * np.sin(4 * np.sum(x_norm, axis=0)) + 0.2 * np.cos(2 * np.sum(x_norm, axis=0))))
        
        # Trigonometric wave component with varying frequencies and amplitude modulation
        wave_term = np.sum(np.sin(3 * np.pi * x_norm) * 
                          np.cos(2 * np.pi * x_norm) * 
                          np.exp(-0.15 * np.sum(x_norm**2, axis=0)) * 
                          (1.0 + 0.2 * np.sin(1.5 * np.sum(x_norm, axis=0))))
        
        # Spherical harmonic-like interaction with enhanced angular component
        sph_harm_term = np.sum(np.sin(3 * np.sqrt(np.sum(x_norm**2, axis=0))) * 
                              np.cos(3 * np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0) * 
                              (1.0 + 0.1 * np.sin(2 * np.sum(x_norm, axis=0))))
        
        # Cross-dimensional interaction with Gaussian peaks and additional sine modulation
        peak_term = 0
        if self.dim > 1:
            peak_term = np.sum(np.exp(-0.4 * (x_norm[0]**2 + x_norm[1]**2)) * 
                              np.sin(6 * np.pi * x_norm[0]) * 
                              np.cos(4 * np.pi * x_norm[1]) * 
                              (1.0 + 0.15 * np.sin(3 * np.sum(x_norm, axis=0))))
        
        # Polynomial interaction term with higher order components
        poly_interaction = 0
        if self.dim > 1:
            poly_interaction = np.sum((x_norm[0] + x_norm[1])**5 + (x_norm[0] - x_norm[1])**3 + 
                                   0.5 * (x_norm[0]**2 + x_norm[1]**2) * np.sin(2 * np.pi * (x_norm[0] + x_norm[1])))
        
        # Combine all terms with different weights
        result = 0.25 * exp_term + 0.3 * wave_term + 0.2 * sph_harm_term + 0.15 * peak_term + 0.1 * poly_interaction
        
        return result