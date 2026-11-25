import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for global attraction
        quadratic_term = np.sum(x_norm**2)
        
        # Chaotic sine wave component with varying frequencies
        chaotic_sine = np.sum(np.sin(10 * np.pi * x_norm + np.sin(3 * np.pi * x_norm)) ** 2)
        
        # Radial basis function component for multiple local minima
        radial_term = np.sum(np.exp(-5 * np.sum((x_norm[:, None] - x_norm[None, :])**2, axis=0)))
        
        # Adaptive curvature term that changes based on dimensionality
        curvature_term = np.sum((x_norm**4) * np.sin(2 * np.pi * x_norm))
        
        # Cross-term interaction for increased complexity
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.cos(np.pi * x_norm[:-1] + np.pi * x_norm[1:]))
        
        # Combine all terms with different weights to create complex landscape
        return 0.5 * quadratic_term + 0.3 * chaotic_sine - 0.2 * radial_term + 0.1 * curvature_term + 0.05 * cross_term