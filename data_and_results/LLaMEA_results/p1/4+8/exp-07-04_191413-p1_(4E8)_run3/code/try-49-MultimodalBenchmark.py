import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Shift input to center the global minimum at (1,1,...,1)
        x_shifted = x - 1.0
        
        # Scale input to [-1, 1] range
        x_scaled = x_shifted / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) * 
                             np.sin(3 * np.pi * x_scaled**2) * np.cos(7 * np.pi * x_scaled))
        
        # Enhanced oscillatory components with radial symmetry
        radial_symmetry = np.sum(np.sin(8 * np.pi * np.sqrt(np.sum(x_scaled**2, axis=0))) * 
                                np.exp(-0.2 * np.sum(x_scaled**2, axis=0)))
        
        # Cross-dimensional interaction with nonlinear coupling
        cross_term = 0.15 * np.sum(np.sin(2 * np.pi * x_scaled[:-1]) * np.cos(2 * np.pi * x_scaled[1:]))
        
        # Additional radial basis function component for multimodality
        rbf_term = np.sum(np.exp(-2 * np.sum((x_scaled.reshape(-1, 1) - x_scaled.reshape(1, -1))**2, axis=0)))
        
        # Adaptive conditioning based on dimensionality
        adaptive_conditioning = 0.05 * self.dim * np.sum(np.abs(x_scaled)**3)
        
        # Combine all terms with different weights
        return quadratic + 0.7 * chaotic_term + 0.3 * radial_symmetry + cross_term + 0.1 * rbf_term + adaptive_conditioning