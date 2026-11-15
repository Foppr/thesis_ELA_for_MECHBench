import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis function component with multiple peaks
        rb_term = np.sum(np.exp(-np.sum((x_scaled[:, np.newaxis] - np.linspace(-1, 1, 10))**2, axis=0)) * 
                        np.sin(10 * np.pi * x_scaled)**2)
        
        # High-frequency sinusoidal oscillations
        sin_term = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) * 
                         np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Cross-terms creating non-separability
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                           np.cos(6 * np.pi * x_scaled[1:]))
        
        # Polynomial with mixed degrees
        poly_term = np.sum(x_scaled**6 + 0.5 * x_scaled**4 + 0.2 * x_scaled**2 + 0.1 * np.abs(x_scaled))
        
        # Adaptive radial scaling with exponential decay
        radial_term = np.sum(np.exp(-0.5 * np.sum(x_scaled**2)) * 
                           np.sin(5 * np.pi * np.linalg.norm(x_scaled))**3)
        
        # Chaotic component with logistic map influence
        chaotic_term = np.sum(np.sin(30 * np.pi * x_scaled**2) * 
                             np.cos(25 * np.pi * x_scaled**2) * 
                             np.sin(20 * np.pi * x_scaled**3))
        
        # Combine all terms with different weights
        return 0.25 * rb_term + 0.2 * sin_term + 0.15 * cross_term + 0.15 * poly_term + 0.1 * radial_term + 0.15 * chaotic_term