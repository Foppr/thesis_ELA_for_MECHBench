import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay term with radial component
        exp_term = np.sum(np.exp(-0.5 * np.sum(x_norm**2, axis=0)) * 
                         (1.0 + 0.5 * np.sin(3 * np.sum(x_norm, axis=0))))
        
        # Trigonometric wave component with varying frequencies
        wave_term = np.sum(np.sin(2 * np.pi * x_norm) * 
                          np.cos(1.5 * np.pi * x_norm) * 
                          np.exp(-0.1 * np.sum(x_norm**2, axis=0)))
        
        # Spherical harmonic-like interaction
        sph_harm_term = np.sum(np.sin(4 * np.sqrt(np.sum(x_norm**2, axis=0))) * 
                              np.cos(2 * np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0))
        
        # Cross-dimensional interaction with Gaussian peaks
        peak_term = np.sum(np.exp(-0.5 * (x_norm[0]**2 + x_norm[1]**2)) * 
                          np.sin(5 * np.pi * x_norm[0]) * 
                          np.cos(3 * np.pi * x_norm[1]) if self.dim > 1 else 0)
        
        # Polynomial interaction term
        poly_interaction = np.sum((x_norm[0] + x_norm[1])**4 + (x_norm[0] - x_norm[1])**2 if self.dim > 1 else 0)
        
        # Combine all terms with different weights
        result = 0.3 * exp_term + 0.25 * wave_term + 0.2 * sph_harm_term + 0.15 * peak_term + 0.1 * poly_interaction
        
        return result