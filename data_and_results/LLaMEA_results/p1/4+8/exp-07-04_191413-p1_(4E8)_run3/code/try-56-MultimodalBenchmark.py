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
        
        # Chaotic sine waves with multiple frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(10 * np.pi * x_scaled) * np.sin(20 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Enhanced oscillatory components with radial symmetry
        radial_symmetry = np.sum(np.sin(3 * np.pi * np.sqrt(np.sum(x_scaled**2, axis=0))) * np.exp(-0.2 * x_scaled**2))
        
        # Additional radial basis function terms for increased multimodality
        rbf_terms = np.sum(np.exp(-5 * (x_scaled**2 + 0.5 * np.sin(4 * np.pi * x_scaled)**2)))
        
        # Cross-dimensional interaction with adaptive weights
        cross_term = 0.15 * np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Add a dynamic conditioning term that varies with dimensionality
        conditioning = 0.05 * np.sum(np.abs(x_scaled)**(1 + 0.1 * self.dim))
        
        # Fractal-like component with self-similar structure
        fractal_component = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Saddle-point landscape enhancement
        saddle_terms = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) * (1 + 0.5 * np.sin(3 * np.pi * x_scaled)))
        
        # Combine all terms with different weights
        return quadratic + 0.7 * chaotic_terms + 0.3 * radial_symmetry + 0.2 * rbf_terms + cross_term + conditioning + 0.25 * fractal_component + 0.1 * saddle_terms