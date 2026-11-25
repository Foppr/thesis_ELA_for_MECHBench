import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic trigonometric polynomial with high frequency components
        chaotic_term = np.sum(np.sin(10 * np.pi * x_norm) * 
                             np.cos(7 * np.pi * x_norm) * 
                             np.sin(3 * np.pi * x_norm) * 
                             np.exp(-0.3 * np.sum(x_norm**2, axis=0)))
        
        # Radial basis function with multiple peaks
        radial_term = np.sum(np.exp(-2.0 * np.sum((x_norm[:, np.newaxis] - x_norm[np.newaxis, :])**2, axis=0)) * 
                           np.sin(5 * np.pi * np.sqrt(np.sum(x_norm**2, axis=0))))
        
        # Cross-dimensional coupling with hyperbolic tangent interactions
        cross_term = np.sum(np.tanh(3 * x_norm[0]) * np.tanh(2 * x_norm[1]) * 
                          np.sin(4 * np.pi * x_norm[0]) * 
                          np.cos(3 * np.pi * x_norm[1]) if self.dim > 1 else 0)
        
        # Spherical harmonic with fractal-like behavior
        sph_harm_term = np.sum(np.sin(6 * np.sqrt(np.sum(x_norm**2, axis=0))) * 
                              np.cos(3 * np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0) * 
                              np.exp(-0.5 * np.sum(x_norm**2, axis=0)))
        
        # Polynomial with mixed degrees and interaction terms
        poly_term = np.sum((x_norm[0]**3 + x_norm[1]**4 + x_norm[0]*x_norm[1])**2 if self.dim > 1 else 0)
        
        # Fractional Brownian motion inspired component
        fbm_term = np.sum(np.sin(2 * np.pi * x_norm) * 
                         np.cos(3 * np.pi * x_norm) * 
                         np.exp(-0.2 * np.sum(x_norm**2, axis=0)) * 
                         np.sin(0.5 * np.sum(x_norm, axis=0)))
        
        # Combine all terms with varying weights and non-linear scaling
        result = 0.25 * chaotic_term + 0.2 * radial_term + 0.15 * cross_term + 0.15 * sph_harm_term + 0.15 * poly_term + 0.1 * fbm_term
        
        return result