import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with radial and angular components
        exp_radial = np.exp(-0.3 * np.sum(x_norm**2, axis=0))
        exp_angular = 1.0 + 0.3 * np.sin(4 * np.sum(x_norm, axis=0))
        exp_term = np.sum(exp_radial * exp_angular)
        
        # Modified trigonometric wave with higher frequency interactions
        wave_term = np.sum(np.sin(3 * np.pi * x_norm) * 
                          np.cos(2.5 * np.pi * x_norm) * 
                          np.exp(-0.15 * np.sum(x_norm**2, axis=0)))
        
        # Enhanced spherical harmonic-like interaction with multiple peaks
        r = np.sqrt(np.sum(x_norm**2, axis=0))
        theta = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0
        sph_harm_term = np.sum(np.sin(5 * r) * np.cos(3 * theta) * 
                              np.exp(-0.2 * r**2))
        
        # Cross-dimensional interaction with multiple Gaussian peaks
        peak_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                for j in range(i + 1, self.dim):
                    dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.1)
                    peak_term += np.exp(-dist**2) * np.sin(6 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Polynomial interaction with mixed terms for increased complexity
        poly_interaction = 0
        if self.dim > 1:
            poly_interaction = np.sum((x_norm[0]**3 + x_norm[1]**3) * 
                                   (x_norm[0]**2 + x_norm[1]**2))
        
        # Combine all terms with different weights
        result = 0.35 * exp_term + 0.25 * wave_term + 0.2 * sph_harm_term + 0.15 * peak_term + 0.05 * poly_interaction
        
        return result