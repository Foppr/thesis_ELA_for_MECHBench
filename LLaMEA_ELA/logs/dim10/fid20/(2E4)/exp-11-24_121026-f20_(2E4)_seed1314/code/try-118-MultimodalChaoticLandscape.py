import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic modulation
        rb_fn = np.sum(np.exp(-np.sum((x_norm[:, None] - np.linspace(-1, 1, 10))**2, axis=0)) * 
                       np.sin(15 * x_norm)**2)
        
        # Sinusoidal oscillation with varying frequencies and chaotic coupling
        sin_term = np.sum(np.sin(10 * x_norm + 0.5 * np.sin(7 * x_norm))**3)
        
        # Cross-dimensional interaction with chaotic weights
        cross_dim = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2))
            cross_dim += weight * (x_norm[i] * x_norm[i+1])**2
        
        # Polynomial chaos component with dynamic scaling
        poly_term = np.sum((x_norm**3 + 0.3 * x_norm**2 - 0.5 * x_norm)**4)
        
        # Multiscale chaotic modulation with exponential decay
        multi_scale = np.sum(np.exp(-np.abs(x_norm)) * np.sin(12 * x_norm) * 
                            (1 + 0.3 * np.cos(9 * x_norm)))
        
        # Additional chaotic sine wave with boundary influence
        boundary_effect = np.sum(np.sin(20 * x_norm) * np.exp(-0.5 * x_norm**2) * 
                               (1 + 0.25 * np.sin(8 * x_norm)))
        
        # Combined fitness function with varying weights
        return 0.5 * rb_fn + 0.3 * sin_term + 0.2 * cross_dim + 0.25 * poly_term + \
               0.15 * multi_scale + 0.1 * boundary_effect